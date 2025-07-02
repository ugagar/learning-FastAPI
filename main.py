from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

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
