import telebot
import psycopg2
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")

SECRET_KEY = os.getenv("SECRET_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        tg_id TEXT NOT NULL,
        username TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

def exists_user(tg_id):
    select = '''
        SELECT * FROM users WHERE tg_id = (%s);
    '''
    cursor.execute(select, (tg_id,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return True
    
def add_user(tg_id, username):
    insert = '''
        INSERT INTO users (tg_id, username) VALUES (%s, %s);
    '''
    cursor.execute(insert, (tg_id, username,))
    connection.commit()

def create_token(tg_id, username):
    payload = {
        "tg_id": tg_id,
        "username": username
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        decode = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decode
    except:
        print("Error")

@bot.message_handler(commands=["start"])
def start(message):
    tg_id = str(message.from_user.id)
    username = message.from_user.username
    if exists_user(tg_id):
        bot.reply_to(message, f"Ձեր թոքենը։ {create_token(tg_id, username)}, Գրեք այն որպեսզի ստանաք տվյալները")
    else:
        add_user(tg_id, username)
        bot.reply_to(message, f"Ձեր թոքենը։ {create_token(tg_id, username)}, Գրեք այն որպեսզի ստանաք տվյալները")

@bot.message_handler(content_types=["text"])
def text(message):
    token = message.text
    result = verify_token(token)
    bot.reply_to(message, str(result))

bot.polling()