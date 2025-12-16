from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from models.nested_items import ItemNested

app = FastAPI()

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=ItemNested)
async def read_item(items_id: str):
    return items[items_id]

@app.patch("/items/{item_id}", response_model=ItemNested)
async def update_item(item_id: str, item: ItemNested):
    stored_item_data = items[item_id]
    stored_item_model = ItemNested(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item