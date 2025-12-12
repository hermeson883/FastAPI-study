from typing import Annotated
from models.form import FormData
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data