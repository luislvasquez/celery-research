import asyncio
from hashlib import new
import time
from uuid import UUID
from datetime import datetime

from api.networks.model import PostRequestPayload
from utils.connection import db_session, async_db_session

def insert_network_query(new_network: PostRequestPayload, status: str):
    return f"""
            INSERT INTO
                networks(
                    name,
                    location,
                    customer,
                    status
                )
            VALUES
                (
                    '{new_network.name}',
                    '{new_network.location}',
                    '{new_network.customer}',
                    '{status}'
                )
            RETURNING id; 
            """

def update_network_status_query(network_uuid: UUID, status: str):
    return f"""
    UPDATE
        networks
    SET
        status = 'ONLINE'
    WHERE
        id = '{network_uuid}';
    """

def update_network_elapsed_timestamps_query(network_uuid: UUID, start: datetime, end: datetime):
    return f"""
    UPDATE
        networks
    SET
        operation_started = '{start}',
        operation_finished = '{end}'
    WHERE
        id = '{network_uuid}';
    """

def fetch_networks_query():
    return f"""
    SELECT
        *
    FROM
        networks;
    """

def get_networks(request_time: datetime):
    with db_session() as db:
        networks = db.execute(fetch_networks_query()).all()
    return networks

def create_network(new_network: PostRequestPayload, request_time: datetime):
    time.sleep(new_network.delayInSeconds)
    with db_session() as db:
        network_uuid = db.execute(insert_network_query(new_network, "ONLINE")).scalar_one()
        db.execute(update_network_elapsed_timestamps_query(network_uuid, request_time, datetime.now()))
        db.commit()

async def async_call_and_storage_create_network(new_network: PostRequestPayload, request_time: datetime):
    async def insert_network(new_network, status):
        insert_query = insert_network_query(new_network, status)
        async with async_db_session() as db:
            network_coroutine = await db.execute(insert_query)
            network_uuid = network_coroutine.scalar_one()
            await db.commit()
        return network_uuid

    async def update_network_status(network_uuid, status, delay_in_seconds):
        update_query = update_network_status_query(network_uuid, status)
        async with async_db_session() as db:
            await asyncio.sleep(delay_in_seconds)
            await db.execute(update_query)
            await db.commit()
    
    async def update_network_elapsed_timestamps(network_uuid, start, end):
        update_query = update_network_elapsed_timestamps_query(network_uuid, start, end)
        async with async_db_session() as db:
            await db.execute(update_query)
            await db.commit()

    network_uuid = await insert_network(new_network, "BUILDING")
        
    loop = asyncio.get_running_loop()
    loop.create_task(update_network_status(network_uuid, "ONLINE", new_network.delayInSeconds))
    loop.create_task(update_network_elapsed_timestamps(network_uuid, request_time, datetime.now()))
