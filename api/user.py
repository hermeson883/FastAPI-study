from typing import Any
from fastapi import FastAPI
from models.userBase import UserBase
from models.userIn import UserIn
from models.user_db import UserInDB

app = FastAPI()

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/")
## Arrow de retorno filtra automaticamente os campos que irá retornar
async def create_user(user: UserIn) -> UserBase:
    return user