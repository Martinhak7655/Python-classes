import uvicorn
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel

connection = psycopg2.connect(
    host="localhost",
    database="mobilesell",
    user="postgres",
    password="MH2012",
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF  NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        country VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

create_table2 = '''
    CREATE TABLE IF NOT EXISTS items(
        id SERIAL PRIMARY KEY,
        header VARCHAR(100) NOT NULL,
        price INTEGER NOT NULL,
        color VARCHAR(100) NOT NULL,
        size INTEGER NOT NULL,
        creata_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table2)
connection.commit()

app = FastAPI()

class User(BaseModel):
    username: str
    surname: str
    age: int
    country: str
    password: str
    mail: str

class DeleteUser(BaseModel):
    id: int

class Items(BaseModel):
    header: str
    price: int
    color: str
    size: int

class DeleteItem(BaseModel):
    id: int

class UpdateItem(BaseModel):
    id: int
    header: str
    price: int
    color: str
    size: int

@app.post("/api/create-user")
def create_user(user: User):
    insert = '''
        INSERT INTO users (username, surname, age, country, password, email) VALUES (%s, %s, %s, %s, %s, %s);
    '''
    cursor.execute(insert, (user.username, user.surname, user.age, user.country, user.password, user.mail,))
    connection.commit()
    return {"succes": True, "message": "This man has been saved"}

@app.delete("/api/delete-user")
def delete_user(user: DeleteUser):
    delete = '''
        DELETE FROM users WHERE id = (%s);
    '''
    cursor.execute(delete, (user.id,))
    connection.commit()
    return {"succes": True, "message": "This man has been deleted"}

@app.post("/api/create-item")
def create_item(item: Items):
    insert = '''
        INSERT INTO items (header, price, color, size) VALUES (%s, %s, %s, %s);
    '''
    cursor.execute(insert, (item.header, item.price, item.color, item.size,))
    connection.commit()
    return {"succes": True, "message": "This item has benn saved"}

@app.delete("/api/delete-item")
def delete_item(item: DeleteItem):
    delete = '''
        DELETE FROM items WHERE id = (%s);
    '''
    cursor.execute(delete, (item.id,))
    connection.commit()
    return {"succes": True, "message": "This item has been deleted"}

@app.put("/api/item-change")
def update_item(item: UpdateItem):
    update = '''
        UPDATE items SET header = (%s), price = (%s), color = (%s), size = (%s) WHERE id = (%s); 
    '''
    cursor.execute(update, (item.header, item.price, item.color, item.size, item.id))
    connection.commit()
    return {"succes": True, "message": "This item has been changed"}

uvicorn.run(app, host="0.0.0.0", port=4532)