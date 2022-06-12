from fastapi import FastAPI
from api.networks.router import router as network_router

app = FastAPI()

app.include_router(network_router)

@app.get("/")
async def root():
    return {"msg": "Backend online!"}
