from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/body")
async def foo():
    return "Bye, World!"

@app.get("/items/0")
async def read_zero_item():
    return {"item_id": "This your item - 0"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
