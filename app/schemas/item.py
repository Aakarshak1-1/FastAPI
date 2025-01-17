from typing import List
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True

class ItemsList(BaseModel):
    items: List[Item]

    class Config:
        from_attributes = True
