from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get-item/")
def get_item(id: Union[str, None] = None):
    return {"id":id}

@app.get("/api/get_username/")
def get_username(username: Union[str, None] = None):
    return {"username" : username}

