from fastapi import FastAPI

from models import Item

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/body")
async def foo():
    return "Bye, World!"

@app.post("/items/")
def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
