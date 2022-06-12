from asyncio import sleep as async_sleep
from datetime import date, datetime
from time import sleep, time
from fastapi import APIRouter, Request

from api.networks.model import PostRequestPayload

router = APIRouter(
    tags=['networks'],
    prefix='/networks',
)

@router.post("/")
def create_network(body: PostRequestPayload):
    start = datetime.now()

    # Heavy CPU process
    sleep(body.delayInSeconds)

    end = datetime.now()
    response = {
        "event": "Network creation",
        "status": "COMPLETED",
        "values": {
            "name": body.name,
            "customer": body.customer,
            "location": body.location,
            "elapsedTime": (end - start).seconds
        }
    }
    return response

@router.post("/async")
async def create_network(body: PostRequestPayload):
    start = datetime.now()
    
    # Heavy CPU process
    async_sleep(body.delayInSeconds)

    end = datetime.now()
    response = {
        "event": "Network creation",
        "status": "TRIGGERED",
        "values": {
            "name": body.name,
            "customer": body.customer,
            "location": body.location,
            "elapsedTime": (end - start).seconds
        }
    }
    return response