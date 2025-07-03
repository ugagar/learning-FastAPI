from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/body")
async def foo():
    return "Bye, World!"

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/0")
async def read_zero_item():
    return {"item_id": "This your item - 0"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    message = ""
    match model_name:
        case ModelName.alexnet:
            message = "Deep Learning FTW!"
        case ModelName.resnet:
            message = "Have some residuals"
        case ModelName.lenet:
            message = "LeCNN all the images"

    return {"model_name": model_name, "message": message}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/books/{book_id}")
async def read_book(book_id: str, q: str | None = None):
    return {"book_id": book_id, "q": q} if q else {"book_id": book_id}
