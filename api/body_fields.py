from fastapi import FastAPI, Body
from typing import Annotated
from models.item import Item

app = FastAPI()

@app.put("/item/{item_id}")
async def update_items(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {
        "item_id": item_id,
        "item": item
    }

    return results