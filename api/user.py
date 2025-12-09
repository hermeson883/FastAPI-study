from typing import Any
from fastapi import FastAPI
from models.userIn import UserIn
from models.userOut import UserOut

app = FastAPI()

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user