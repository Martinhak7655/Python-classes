import telebot
from telebot import types
import psycopg2

BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="telegrambot",
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
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Mutq Gorcel", callback_data="Mutq_Gorcel")
    button2 = types.InlineKeyboardButton("Grancvel", callback_data="Grancvel")
    markup.add(button1, button2)
    bot.reply_to(message, "Hi im Bot Choose Button", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def signin(call):
    if call.data == "Grancvel":
        bot.send_message(call.message.chat.id, "Ok Lets Type Your Username")
        @bot.message_handler(content_types=["text"])
        def insert_info(message):
            if "username" not in user_data:
                username = message.text
                user_data["username"] = username
                bot.reply_to(message, "Ok! Now Lets Type Your Password")
            else:
                password = message.text
                user_data["password"] = password
                insert = '''
                    INSERT INTO users (username, password) VALUES (%s, %s)
                '''
                cursor.execute(insert, (user_data["username"], user_data["password"],))
                connection.commit()
                bot.reply_to(message, "Congratulations❤️! Your Account has been saved")
    else:
        bot.send_message(call.message.chat.id, "Ok! Now Lets Type Your account Password")
        @bot.message_handler(content_types=["text"])
        def get_info(message):
            password2 = message.text
            select = '''
                SELECT * FROM users WHERE password = (%s);
            '''
            cursor.execute(select, (password2,))
            connection.commit()
            users = cursor.fetchone()
            bot.reply_to(message, f"Username: {users[1]}, Password: {users[2]}")

bot.polling()