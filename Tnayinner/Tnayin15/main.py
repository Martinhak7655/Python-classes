from typing import Union
from fastapi import FastAPI
import psycopg2

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="fastapi",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL,
        age VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

select = '''
    SELECT * FROM users;
'''
cursor.execute(select)
connection.commit()
user = cursor.fetchall()

@app.get("/")
def user_data():
    try:
        return {"name": user[0][1], "surname": user[0][2], "age": user[0][3], "country": user[0][4]}
    except:
        print("Error")