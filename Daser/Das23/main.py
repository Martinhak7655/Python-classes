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

user_data = {}

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton("/signin")
    markup.add(btn1)
    bot.reply_to(message, "Hi! I'm Bot", reply_markup=markup)

@bot.message_handler(commands=["signin"])
def signin(message):
    bot.reply_to(message, "Username:")

@bot.message_handler(content_types=["text"])
def get_username(message):
    if "username" not in user_data:
        username = message.text
        user_data["username"] = username
        bot.reply_to(message, "Now lets type your Password")
    else:
        password = message.text
        user_data["password"] = password
        insert = '''
            INSERT INTO users (username, password) VALUES (%s, %s);
        '''
        cursor.execute(insert, (user_data["username"], user_data["password"]))
        connection.commit()
        bot.reply_to(message, "Thank!, Your account has been saved")

bot.polling()