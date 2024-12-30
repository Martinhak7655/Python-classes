from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api/get-id/{id}")
def get_id(id: int):
    return {"user-id": id}

@app.get("/api/get-username/{username}")
def get_username(username: str):
    return {"user-username": username}

uvicorn.run(app, host="0.0.0.0", port=5400)