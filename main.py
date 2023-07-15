from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/normal-root")
def normal_root():
    return {"message": "Hello world!"}
