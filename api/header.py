from typing import Annotated
from fastapi import FastAPI, Header
from models.headers import CommonHeaders

app = FastAPI()

@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()] = None):
    return headers

