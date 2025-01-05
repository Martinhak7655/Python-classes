from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class User(BaseModel):
    username: str
    surname: str
    age: int
    country: str
    password: str
    email: str

class Item(BaseModel):
    header: str
    price: int
    color: str
    size: int

class DeleteItem(BaseModel):
    id: int

@app.post("/api/create")
def user(user: User):
    return {"succes": True}

@app.post("/api/create-item")
def item(item: Item):
    return {"succes": True}

@app.put("/api/item-update")
def update(item: Item):
    return {"succes": True, "message": "This item has been changed"}

@app.delete("/api/delete-item")
def delete(item: DeleteItem):
    return {"succes": True, "message": "This item has been deleted"}

uvicorn.run(app, host="0.0.0.0", port=3456)

#postgresum zroyic mihat baza sarqel ogtatereri tvyalner mekel apranqeri tvyalner+1
#nor ogtaterer grancel posti mijocov 
#ete nuyn maylov mard ka chrgancel
#mardkanc kareliya jnjel
#kareliya avelacnel apranqner
#apranqery kareliya jnjel
#apranqey kareliya popoxel