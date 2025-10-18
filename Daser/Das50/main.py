import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")

def create_token(username, mail):
    payload = {
        "username": username,
        "mail": mail
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

username = input("Enter username:  ")
mail = input("Enter Mail:  ")

patasxan = create_token(username, mail)
print(patasxan)

def verify_token(token):

    try:
        decode = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decode
    except:
        print("Error")

print(verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik1hcnRpbjU1NjYiLCJtYWlsIjoibWFydGluaGFrb2J5YW4ifQ.dqECmRF88Y58hS2n3e_yo3IHCjNVC3GoBra7QVDpzwo"))