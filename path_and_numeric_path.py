from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/item/{item_id}")
async def read_items(
    item_id: Annotated[
        int, 
        Path(title="The id of the item to get", ge=0, le=1000)
    ],
    q: str,
    size: Annotated[
        float,
        Query(gt=0, lt=10.5)
    ]
):
    results = {
        "item_id": item_id
    }

    if q:
        results.update({"q": q})
    if size:
        results.update({
            "size": size
        })
        
    return results