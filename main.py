from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/normal-root")
def normal_root():
    return {"message": "Hello world!"}


"""
 order matters, items/test should be bfore items/{item_id}
"""


@app.get("/items/test")
async def read_item2():
    return {"item2": "test2"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
