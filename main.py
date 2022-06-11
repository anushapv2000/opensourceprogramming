#from typing import Union

from fastapi import FastAPI

app = FastAPI()

chairs = ["cat","dog"]
@app.get("/")
async def showMessage():
    return {"response": "this is root"}
#def read_root():
#        return {"Hello": "World"}
@app.get("/chairs")
async def getchairs1():
    return getchairs()

@app.post("/chairs")
async def addchairs2(new):
    chairs.append(new)
    return {"result":True,"chairs":chairs}


def getchairs():
    return ["red","blue"]
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#        return {"item_id": item_id, "q": q}
