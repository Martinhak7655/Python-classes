import jwt
import psycopg2
import uvicorn
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import bcrypt


load_dotenv()
app = FastAPI()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

JWT_CODE = os.getenv("JWT_SECRET")

connection = psycopg2.connect(
    host="localhost",
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        mail TEXT NOT NULL,
        password BYTEA NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

create_table2 = '''
    CREATE TABLE IF NOT EXISTS admins(
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        mail TEXT NOT NULL,
        password BYTEA NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table2)
connection.commit()

def create_token(username):
    payload = {
        "username": username
    }
    token = jwt.encode(payload, JWT_CODE, algorithm="HS256")
    return token

class SignIn(BaseModel):
    username: str
    password: str

class SignUp(BaseModel):
    username: str
    mail: str
    password: str

class SignInAdmin(BaseModel):
    username: str
    password: str

class SignUpAdmin(BaseModel):
    username: str
    mail: str
    password: str

@app.post("/api/signin")
def signin(user: SignIn):
    username = user.username
    password = user.password.encode()

    select = '''
        SELECT * FROM users WHERE username = (%s);
    '''
    cursor.execute(select, (username,))
    connection.commit()
    users = cursor.fetchone()

    if user:
        db_password = bytes(users[3])
        if bcrypt.checkpw(password, db_password):
            return {"succes": True, "message": "Welcome to your account", "token": create_token(username)}
        else:
            return {"succes": False, "message": "Your password is incorrect"}

@app.post("/api/create_user")
def SignUp(user: SignUp):
    username = user.username
    mail = user.mail
    password = user.password.encode()

    password_hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))

    insert = '''
        INSERT INTO users (username, mail, password) VALUES (%s, %s, %s);
    '''
    cursor.execute(insert, (username, mail, password_hashed,))
    connection.commit()
    return {"succes": True, "message": "You has been registered", "token": create_token(username)}

@app.post("/api/signin_admin")
def signin(user: SignIn):
    username = user.username
    password = user.password.encode()

    select = '''
        SELECT * FROM admins WHERE username = (%s);
    '''
    cursor.execute(select, (username,))
    connection.commit()
    users = cursor.fetchone()

    if user:
        db_password = bytes(users[3])
        if bcrypt.checkpw(password, db_password):
            return {"succes": True, "message": "Welcome to your account", "token": create_token(username)}
        else:
            return {"succes": False, "message": "Your password is incorrect"}

@app.post("/api/create_user")
def SignUp(user: SignUp):
    username = user.username
    mail = user.mail
    password = user.password.encode()

    password_hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))

    insert = '''
        INSERT INTO admins (username, mail, password) VALUES (%s, %s, %s);
    '''
    cursor.execute(insert, (username, mail, password_hashed,))
    connection.commit()
    return {"succes": True, "message": "You has been registered", "token": create_token(username)}

uvicorn.run(app, host="0.0.0.0", port=7600)
