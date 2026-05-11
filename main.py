from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: ShopInfo
    items: List[Item]

app = FastAPI()

@app.get("/")
async def index():
    return { "message": "Hellow World" }

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return { "item_id": item_id }

@app.get("/countriies/")
async def country_info(country_name: str, country_id: int):
    return{
        "country_name": country_name,
        "country_id": country_id
    }

@app.get("/countries/")
async def contry(country_name:Optional[str] = None, country_id:Optional[int] = None):
    return {
        "country_name":country_name,
        "country_id": country_id
    }

@app.post("/item/")
async def create_item(item: Item):
    return item

@app.post("/items/")
async def read_item(data: Data):
    return { "data": data }