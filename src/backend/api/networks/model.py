from typing import Optional
from enum import Enum
from pydantic import BaseModel, conint

class NetworkLocation(str, Enum):
    america = "america"
    asia = "asia"
    europe = "europe"


class PostRequestPayload(BaseModel):
    customer: str
    name: str
    location: NetworkLocation
    delayInSeconds: Optional[conint(ge=0)] = 0
