import psycopg2
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="adminpanelfastapi",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

tasks = '''
    CREATE TABLE IF NOT EXISTS tasks(
        id SERIAL PRIMARY KEY,
        password VARCHAR(100) NOT NULL,
        task VARCHAR(100) NOT NULL,
        procces BOOLEAN NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(tasks)
connection.commit()

class CreateUser(BaseModel):
    username: str
    password: str

class DeleteUser(BaseModel):
    id: int

class Task(BaseModel):
    id: int
    task: str

class SeeTask(BaseModel):
    password: str

class UpdateProcces(BaseModel):
    password: str
    procces: bool

class SeeAdminTask(BaseModel):
    password: str

@app.post("/api/create-user")
def create_user(user: CreateUser):
    insert = '''
        INSERT INTO users (username, password) VALUES (%s, %s);
    '''
    cursor.execute(insert, (user.username, user.password,))
    connection.commit()
    insert2 = '''
        INSERT INTO tasks (password, task, procces) VALUES (%s, %s, %s);
    '''
    cursor.execute(insert2, (user.password, "Der Arajadranq chka", False))
    connection.commit()
    return {"succes": True, "message": "This man has been saved"}

@app.delete("/api/delete-user")
def delete_user(user: DeleteUser):
    delete = '''
        DELETE FROM users WHERE id = (%s);
    '''
    cursor.execute(delete, (user.id,))
    connection.commit()
    task_delete = '''
        DELETE FROM tasks WHERE id = (%s);
    '''
    cursor.execute(task_delete, (user.id,))
    connection.commit()
    return {"succes": True, "message": "This Man has been deleted"}

@app.put("/api/update-task")
def update(task: Task):
    update = '''
        UPDATE tasks SET task = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (task.task, task.id,))
    connection.commit()
    return {"succes": True, "message": "This task has been updated"}

@app.post("/api/seetask")
def seetask(task: SeeTask):
    try:
        select = '''
            SELECT * FROM tasks WHERE password = (%s);
        '''
        cursor.execute(select, (task.password,))
        connection.commit()
        task = cursor.fetchone()

        if task:
            return {"succes": True, "task": task[2], "message": "This item!!"}
    except:
        print("Error")

@app.put("/api/change-procces")
def procces(task: UpdateProcces):
    update = '''
        UPDATE tasks SET procces = (%s) WHERE password = (%s);
    '''
    cursor.execute(update, (task.procces, task.password,))
    connection.commit()
    return {"succes": True, "message": "This procces has been changed"}

@app.post("/api/seeadmintask")
def seeadmintask(task: SeeAdminTask):
    try:
        select = '''
            SELECT * FROM tasks WHERE password = (%s);
        '''
        cursor.execute(select, (task.password,))
        connection.commit()
        task = cursor.fetchone()
        if task:
            return {"succes": True, "procces": task[3]}
    except:
        print("Error")

uvicorn.run(app, host="0.0.0.0", port=3876)