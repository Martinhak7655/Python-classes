from dotenv import load_dotenv
import os
import psycopg2
import jwt



load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")

def create_token(username, mail):
    payload = {
        "username": username,
        "mail": mail
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

input1 = input("Enter username:  ")
input2 = input("Enter mail:  ")

patasxany = create_token(input1, input2)
print(patasxany)

def verify_token(token):
    try:
        decode = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decode
    except:
        print("Error")

print(verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik1hcnRpbiIsIm1haWwiOiJtYXJ0aW4yMzMzQGdhbWlsLmNvbSJ9.bcOOPR4UsoP4qhh3oXw3Mq9SJA11oaTHr5b8OxpA1t4"))

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")

# token = os.getenv("BOT_TOKEN")

# print(token)

connection = psycopg2.connect(
    host="localhost",
    database=db_name,
    user=db_user,
    password=db_password
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        tg_id TEXT NOT NULL,
        username TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

#Stexcel cankacac bot, vori informacian pahpanvelua .env um 