from fastapi import FastAPI, Depends
from enum import Enum
from typing import Annotated

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


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def read_item_new(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description":
             """This is an amazing item that has a long description"""}
        )
    return item


async def common_parameters(q: str | None = None, skip: int = 0,
                            limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/dependencies/items")
async def read_users_dependencies(commons: Annotated[dict, Depends
                                                     (common_parameters)]):
    return
