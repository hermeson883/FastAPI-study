from fastapi.encoders import jsonable_encoder
from datetime import datetime
from fastapi import FastAPI
from models.nested_items import ItemNested

fake_db = {}

app = FastAPI()

@app.put("/items/{id}")
def update_item(id: str, item: ItemNested):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
