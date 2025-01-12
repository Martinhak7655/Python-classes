import psycopg2
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import uvicorn
import requests

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="website",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        mail VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        friends INTEGER DEFAULT 0
    );
'''
cursor.execute(create_table)
connection.commit()

#insert

# insert = '''
#     INSERT INTO users (username, mail, password, age, friends) VALUES (%s, %s, %s, %s, %s);
# '''
# cursor.execute(insert, ("Suren", "suren3444@gmail.com", "Suren345", 25, 0,))
# connection.commit()

#select

# select = '''
#     SELECT * FROM users 
# '''
# cursor.execute(select)
# connection.commit()
# users = cursor.fetchall()
# for x in users:
#     print(f"username: {x[1]}, mail: {x[2]}, password: {x[3]}, age: {x[4]}, friends: {x[5]}")

#update

# update = '''
#     UPDATE users SET friends = friends + 1 WHERE mail = (%s);
# '''
# cursor.execute(update, ("armen3444@gmail.com",))
# connection.commit()

#delete 

# delete = '''
#     DELETE FROM users WHERE mail = (%s);
# '''
# cursor.execute(delete, ("suren3444@gmail.com",))
# connection.commit()

class User(BaseModel):
    username: str
    mail: str
    password: str
    age: int
    friends: int

class Change(BaseModel):
    password: str

class Delete(BaseModel):
    password: str

@app.get("/api/get-id/")
def get_id(id: Union[int, None] = None):
    return {"id": id}

@app.get("/api/get-id/{id}")
def get_id2(id: int):
    return {"id": id}

@app.post("/api/create-user")
def create_user(user: User):
    insert = '''
        INSERT INTO users (username, mail, password, age, friends) VALUES (%s, %s, %s, %s, %s);
    '''
    cursor.execute(insert, (user.username, user.mail, user.password, user.age, user.friends,))
    connection.commit()
    return {"succes": True, "message": "This man has been saved"}

@app.put("/api/change-follower")
def change(user: Change):
    update = '''
        UPDATE users SET friends = friends + 1 WHERE password = (%s);
    '''
    cursor.execute(update, (user.password,))
    connection.commit()
    return {"succes": True, "message": "This man followr has been changed"}

@app.delete("/api/delete-user")
def delete(user: Delete):
    delete = '''
        DELETE FROM users WHERE password = (%s);
    '''
    cursor.execute(delete, (user.password,))
    connection.commit()
    return {"succes": True, "message": "This man has been deleted"}

# try: 
#     country = input("Enter Country Name")

#     res = requests.get(f"https://restcountries.com/v3.1/name/{country}")
#     data = res.json()
#     print(f"population: {data[0]["population"]}")
# except:
#     print("Error")

uvicorn.run(app, host="0.0.0.0", port=3456)