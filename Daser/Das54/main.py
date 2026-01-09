import telebot
from telebot import types
import os
import psycopg2

SAVE_FOLDER = "./images"
os.makedirs(SAVE_FOLDER, exist_ok=True)


BOT_TOKEN = "8220373377:AAHSxaZ-szfTV_TllGw6ZDrEt28MXv45Dk0"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="imagedownloader",
    user="postgres",
    password = "MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        image_link TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Save Image", callback_data="save")
    btn2 = types.InlineKeyboardButton("Show image", callback_data="show")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Select button", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "save":
        bot.send_message(call.message.chat.id, "Please Send a image")
    elif call.data == "show":
        bot.send_message(call.message.chat.id, "Wait a minute")
        bot.register_next_step_handler(call.message, show_image)



@bot.message_handler(content_types=["photo"])
def save(message):
    username = message.from_user.username
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    with open(file_path, "wb") as f:
        f.write(download_file)
    insert = '''
        INSERT INTO images (username, image_link) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, file_name,))
    connection.commit()

def show_image(message):
    username = message.from_user.username
    print(username)
    select = '''
        SELECT * FROM images WHERE username = (%s);
    '''
    cursor.execute(select, (username,))
    connection.commit()
    users = cursor.fetchall()

    for user in users:
        bot.send_photo(message.chat.id, open(f"./images/{user[2]}", "rb"))

bot.polling()