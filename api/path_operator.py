from fastapi import FastAPI, status
from models.nested_items import ItemNested
from models.enumerate import Tags

app = FastAPI()

@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]

@app.post("/items/", response_model=ItemNested, summary="Create a Item", response_description="The created item",)
async def create_item(item: ItemNested):
    """
        Create an item with all the information:

        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tax**: if the item doesn't have tax, you can omit this
        - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]