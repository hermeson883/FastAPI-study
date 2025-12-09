from typing import Annotated
from fastapi import FastAPI, Cookie
from models.coockies import Coockies

app = FastAPI()

@app.get("/items/")
async def read_items(coockies: Annotated[Coockies, Cookie()]):
    return coockies