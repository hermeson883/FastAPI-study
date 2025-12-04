from typing import Annotated, Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query
from models.filter_parameters import FilterParams

app = FastAPI()

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query