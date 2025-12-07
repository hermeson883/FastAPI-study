from models.nested_items import ItemNested
from pydantic import BaseModel

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[ItemNested]