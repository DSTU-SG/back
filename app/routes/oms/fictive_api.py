from fastapi import APIRouter
from pydantic import BaseModel

fictive = APIRouter()

class Item(BaseModel):
    data: dict

@fictive.post("/metadata_api")
def read_item(item: Item):
    # Здесь может быть логика обработки данных
    return {"message": "Data received", "code": "OK"}