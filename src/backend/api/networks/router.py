import asyncio
from datetime import date, datetime
from fastapi import APIRouter, Request

from api.networks.model import PostRequestPayload
from api.networks import controller

router = APIRouter(
    tags=['networks'],
    prefix='/networks',
)

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
            "elapsedTime": elapsed_time.seconds
        }
    }
    return response

@router.post("/async_endpoint/")
async def async_create_network(body: PostRequestPayload):
    start = datetime.now()
    
    # Heavy CPU process
    asyncio.create_task(controller.async_call_create_network(body, request_time=start))

    elapsed_time = datetime.now() - start
    response = {
        "event": "Network creation",
        "status": "TRIGGERED",
        "values": {
            "name": body.name,
            "customer": body.customer,
            "location": body.location,
            "elapsedTime": elapsed_time.seconds
        }
    }
    return response
