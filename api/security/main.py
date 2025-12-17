from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

app = FastAPI()

oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oath2_scheme)]):
    return {
        "token": token
    }

