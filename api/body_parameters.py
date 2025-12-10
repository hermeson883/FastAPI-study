from fastapi import FastAPI, Path, Body
from models.item import Item
from models.userIn import User
from typing import Annotated

app = FastAPI()

@app.put("/items/{item_id}")
async def updated_item(
    item_id : Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None
):
    results = {
        "item_id": item_id, 
        "item": item, 
        "user": user,
        "importance": importance
    }

    if q:
        results.update({"q" : q})

    return results
