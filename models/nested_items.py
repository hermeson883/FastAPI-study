from pydantic import BaseModel
from models.image import Image

class ItemNested(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float
    tags: set[str] = []
    image: list[Image] | None = None