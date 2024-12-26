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
users = cursor.fetchall()

@app.get("/")
def user_data():
    try:
        if users:
            user_list = []
            for user in users:
                user_data = {
                    "name": user[1], 
                    "surname": user[2], 
                    "age": user[3], 
                    "country": user[4] 
                }
                user_list.append(user_data)
            return {"users": user_list}
        else:
            return {"message": "Not Found"}
    except:
        print("Error")