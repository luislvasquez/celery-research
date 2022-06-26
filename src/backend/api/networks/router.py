import asyncio
from datetime import date, datetime
from fastapi import APIRouter, Request

from api.networks.model import PostRequestPayload
from api.networks import controller

router = APIRouter(
    tags=['networks'],
    prefix='/networks',
)

@router.get("/")
def get_networks():

    start = datetime.now()
    # Heavy CPU process
    networks_list = controller.get_networks(request_time=start)
    elapsed_time = datetime.now() - start
    response = {
        "event": "Networks fetching",
        "status": "COMPLETED",
        "values": {
            "data": networks_list,
            "total": len(networks_list),
        }
    }
    return response

@router.post("/")
def create_network(body: PostRequestPayload):
    start = datetime.now()

    # Heavy CPU process
    controller.create_network(body, request_time=start)

    elapsed_time = datetime.now() - start
    response = {
        "event": "Network creation",
        "status": "COMPLETED",
        "values": {
            "name": body.name,
            "customer": body.customer,
            "location": body.location,
            "elapsedTime": elapsed_time.seconds,
            "total": 1,
        }
    }
    return response

@router.post("/async/")
async def full_async_create_network(body: PostRequestPayload):
    start = datetime.now()
    
    # Heavy CPU process
    await controller.async_call_and_storage_create_network(body, request_time=start)

    elapsed_time = datetime.now() - start
    response = {
        "event": "Network creation",
        "status": "TRIGGERED",
        "values": {
            "name": body.name,
            "customer": body.customer,
            "location": body.location,
            "elapsedTime": elapsed_time.seconds,
            "total": 1,
        }
    }
    return response
