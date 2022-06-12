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

def update_network_status(network_uuid: UUID, status: str):
    return f"""
    UPDATE
        networks
    SET
        status = 'ONLINE'
    WHERE
        id = '{network_uuid}';
    """

def update_network_elapsed_timestamps(network_uuid: UUID, start: datetime, end: datetime):
    return f"""
    UPDATE
        networks
    SET
        operation_started = '{start}',
        operation_finished = '{end}'
    WHERE
        id = '{network_uuid}';
    """

def create_network(new_network: PostRequestPayload, request_time: datetime):
    time.sleep(new_network.delayInSeconds)
    with db_session() as db:
        network_uuid = db.execute(insert_network_query(new_network, "ONLINE")).scalar_one()
        db.execute(update_network_elapsed_timestamps(network_uuid, request_time, datetime.now()))
        db.commit()

async def async_call_create_network(new_network: PostRequestPayload, request_time: datetime):
    with db_session() as db:
        network_uuid = db.execute(insert_network_query(new_network, "BUILDING")).scalar_one()
        db.commit()

        time.sleep(new_network.delayInSeconds)
        db.execute(update_network_status(network_uuid, "CREATING"))
        db.execute(update_network_elapsed_timestamps(network_uuid, request_time, datetime.now()))
        db.commit()
