from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hi():
    return {"Hello": "World"}

@app.get("/get/user_data")
def user_data():
    return {"name": "Ruben", "surname": "Gevorgyan", "age": "24", "country": "Italy"}