import telebot
from telebot import types
import psycopg2

#1
# for i in range(1, 10):
#     print(f"{i}: Hello World")

#2
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

#3 

# new_list = [1, 1, 4]
# gumar = 0

# for i in new_list:  
#     gumar = gumar + i
# print(gumar)

# new_list = [3, 4, 8, 3, 2]
# gumar = 0
# qanak = len(new_list)

# for i in range(0, len(new_list)):
#     gumar += new_list[i]

# print(gumar // qanak)


#5

# username = input("Enter Your Username:  ")

# def func(text):
#     return f"Your username is: {text}"

# patasxan = func(username)
# print(patasxan)

#6

connection = psycopg2.connect(
    host="localhost",
    database="qnutyun11",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        tg_id TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

def add_user(username, tg_id):
    insert = '''
        INSERT INTO users (username, tg_id) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, tg_id,))
    connection.commit()


BOT_TOKEN = "8125730473:AAEBNEY5R8ZAJyBYevwET0GWUYkM357kIgQ"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Register", callback_data="register")
    markup.add(btn1)
    bot.reply_to(message, "Select the button", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    username = call.from_user.username
    tg_id = str(call.from_user.id)
    if call.data == "register":
        add_user(username, tg_id)
        bot.send_message(call.message.chat.id, "Welcome To Your Page")


bot.polling()