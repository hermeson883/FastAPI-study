from fastapi import FastAPI, Path, Query
from typing import Annotated
from models.filter_parameters import FilterParams

app = FastAPI()

@app.get("/item/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query