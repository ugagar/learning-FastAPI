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
