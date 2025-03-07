from fastapi import FastAPI
import psycopg2
import uvicorn
from pydantic import BaseModel

connection = psycopg2.connect(
    host="localhost",
    database="dbgrancum2",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

app = FastAPI()

create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

class SignUp(BaseModel):
    username: str
    password: str

class SignIn(BaseModel):
    password: str

@app.post("/api/signup")
def signup(user: SignUp):
    insert = '''
        INSERT INTO users (username, password) VALUES (%s, %s);
    '''
    cursor.execute(insert, (user.username, user.password,))
    connection.commit()
    return {"succes": True, "message": "Your account has been saved"}

@app.post("/api/signin")
def signin(user: SignIn):
    select = '''
        SELECT * FROM users WHERE password = (%s);
    '''
    cursor.execute(select, (user.password,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return {"succes": True, "message": f"Բարի գալուստ ձեր աշխատանքային պանել {user[1]}"}

uvicorn.run(app, host="0.0.0.0", port=8000)