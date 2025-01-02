import psycopg2
from typing import Union
from fastapi import FastAPI

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="fastapidas",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

@app.get("/api/get-id/")
def get_id(id: Union[int, None] = None):
    try:
        select = '''
            SELECT * FROM users WHERE id = (%s);
        '''
        cursor.execute(select, (id,))
        connection.commit()
        user = cursor.fetchone()

        if user:
            return {"user": user[0], "username": user[1], "password": user[2]}
        else:
            return {"message": "This man not found"}
    except:
        print("Error")