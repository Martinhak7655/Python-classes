import telebot
import psycopg2
from telebot import types

BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database='signinbot',
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

@bot.message_handler(commands=["start"])
def signin(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton("/signin")
    markup.add(btn1)
    bot.reply_to(message, "Hi! I'm Bot", reply_markup=markup)

@bot.message_handler(commands=["signin"])
def signin(message):
    bot.reply_to(message, "ok lets type your username and password")

@bot.message_handler(content_types=["text"])
def types2(message):
    username = message.text
    password = message.text
    insert = '''
        INSERT INTO users (username, password) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, password,))
    connection.commit()

bot.polling()