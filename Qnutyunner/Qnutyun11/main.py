import telebot
import os
import psycopg2
from telebot import types

SAVE_FOLDER = "./images"
os.makedirs(SAVE_FOLDER, exist_ok=True)
user_data = {}

BOT_TOKEN = "8038569914:AAEApACBenBklgnBrjkFO00zZ4QPREyJ8zY"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="pinterest",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        image TEXT NOT NULL,
        category VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Ուղարկել Նկար", callback_data="uxarkel")
    button2 = types.InlineKeyboardButton("Ստանալ Նկար", callback_data="stanal")
    markup.add(button1, button2)
    bot.reply_to(message, "Խնդրում եմ նշեք կոճակներից որև է մեկը", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = str(call.from_user.id)
    if call.data == "uxarkel":
        user_data[user_id] = {}
        bot.send_message(call.message.chat.id, "Ուղարկեք նկար")
    if call.data == "stanal":
        bot.send_message(call.message.chat.id, "Գրեք կատեգորյան")
        bot.register_next_step_handler(call.message, show_photo)

@bot.message_handler(content_types=["photo"])
def photo(message):
    photo = message.photo[-1]
    user_id = str(message.from_user.id)
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    with open(file_path, "wb") as f:
        f.write(download_file)
    user_data[user_id]["photo"] = file_name
    bot.reply_to(message, "խՆդրում ենք գրեք կատեգորյան")
    bot.register_next_step_handler(message, category)

def category(message):
    username = message.from_user.username
    user_id = str(message.from_user.id)
    category = message.text

    user_data[user_id]["category"] = category

    insert = '''
        INSERT INTO users (username, image, category) VALUES (%s, %s, %s)
    '''
    cursor.execute(insert, (username, user_data[user_id]["photo"], user_data[user_id]["category"],))
    connection.commit()
    del user_data[user_id]["photo"]
    del user_data[user_id]["category"]

def show_photo(message):
    category = message.text

    select = '''
        SELECT * FROM users WHERE category = (%s);
    '''
    cursor.execute(select, (category,))
    connection.commit()
    users = cursor.fetchall()
    for user in users:
        bot.send_photo(message.chat.id, open(f"./images/{user[2]}", "rb"))
        bot.reply_to(message, f"Ստեղծողը՝ {user[1]}")
bot.polling()
    