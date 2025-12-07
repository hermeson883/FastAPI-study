from fastapi import FastAPI
from models.offer import Offer

app = FastAPI()

@app.post("/offer/")
async def create_offer(offer: Offer):
    return offer