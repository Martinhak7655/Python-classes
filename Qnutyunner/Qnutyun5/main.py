import telebot
import psycopg2
from telebot import types
import requests

BOT_TOKEN = "7885441155:AAHBYjMHJ_XnyMz0N70Grr7CHspp0mHt5-8"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="bottodolist",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()


task_data = {}
create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        telegram_id VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

create_table2 = '''
    CREATE TABLE IF NOT EXISTS tasks(
        id SERIAL PRIMARY KEY,
        telegram_id VARCHAR(100) NOT NULL,
        task VARCHAR(100) NOT NULL,
        task_password VARCHAR(100) NOT NULL,
        procces VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table2)
connection.commit()

# connection = psycopg2.connect(
#     host="localhost",
#     database="searchcountry",
#     user="postgres",
#     password="MH2012"
# )
# cursor = connection.cursor()

# create_table = '''
#     CREATE TABLE IF NOT EXISTS country(
#         id SERIAL PRIMARY KEY,
#         country VARCHAR(100) NOT NULL,
#         image VARCHAR(300) NOT NULL,
#         create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
# '''
# cursor.execute(create_table)
# connection.commit()



# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.reply_to(message, "Գրեք Բարև")

# @bot.message_handler(content_types=["text"])
# def text(message):
#     text = message.text
#     if text == "Բարև":
#         bot.reply_to(message, ("Բարև"))


# @bot.message_handler(commands=["start"])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Ավելացնել Պատմություն", callback_data="avelacnel")
#     button2 = types.InlineKeyboardButton("Փնտրել Երկիրը", callback_data="pntrel")
#     markup.add(button1, button2)
#     bot.reply_to(message, "Բարև ձեզ, ընտրեք կոճակներից որևէ մեկը", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == "avelacnel":
#         bot.send_message(call.message.chat.id, "Գրեք երկրի անունը")
#         bot.register_next_step_handler(call.message, insert_country)
#     elif call.data == "pntrel":
#         bot.send_message(call.message.chat.id, "Գրեք Երկրի Անունը")
#         bot.register_next_step_handler(call.message, search_country)

# def insert_country(message):
#     country_name = message.text

#     res = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
#     data = res.json()
#     insert = '''
#         INSERT INTO country (country, image) VALUES (%s, %s);
#     '''
#     cursor.execute(insert, (country_name, f"{data[0]["flags"]["png"]}",))
#     connection.commit()
#     bot.reply_to(message, "Ձեր պատմությունը ավելացվեց")

# def search_country(message):
#     country_name = message.text

#     res = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
#     data = res.json()
#     select = '''
#         SELECT * FROM country WHERE country = (%s);
#     '''
#     cursor.execute(select, (country_name,))
#     connection.commit()
#     country_flag = cursor.fetchone()
#     if country_flag:
#         bot.reply_to(message, f"{data[0]["flags"]["png"]}")

def add_user(username, telegram_id):
    insert = '''
        INSERT INTO users (username, telegram_id) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, str(telegram_id),))
    connection.commit()

def user_exists(telegram_id):
    select = '''
        SELECT * FROM users WHERE telegram_id = (%s);
    '''
    cursor.execute(select, (str(telegram_id),))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return True
    
@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.first_name
    telegram_id = str(message.from_user.id)
    if user_exists(telegram_id):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Ավելացնել առաջադրանք", callback_data="avelacnel")
        button2 = types.InlineKeyboardButton("Ջնջել բոլոր կատարված առաջադրանքները", callback_data="jnjel")
        button3 = types.InlineKeyboardButton("Տեսնել Իմ առաջադրանքները", callback_data="tesnel")
        button4 = types.InlineKeyboardButton("Նշել որպես կատարված", callback_data="nshel")
        markup.add(button1, button2, button3, button4)
        bot.reply_to(message, "Ընտրեք կոճակներից որևէ մեկը", reply_markup=markup)
    else:
        add_user(username, telegram_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Ավելացնել առաջադրանք", callback_data="avelacnel")
        button2 = types.InlineKeyboardButton("Ջնջել բոլոր կատարված առաջադրանքները", callback_data="jnjel")
        button3 = types.InlineKeyboardButton("Տեսնել Իմ առաջադրանքները", callback_data="tesnel")
        button4 = types.InlineKeyboardButton("Նշել որպես կատարված", callback_data="nshel")
        markup.add(button1, button2, button3, button4)
        bot.reply_to(message, "Ընտրեք կոճակներից որևէ մեկը", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = str(call.from_user.id)

    if call.data == "avelacnel":
        task_data[user_id] = {}
        bot.send_message(call.message.chat.id, "Գրեք առաջադրանքը")
        bot.register_next_step_handler(call.message, get_task_text)
    elif call.data == "jnjel":
        delete_task(call.message, user_id)
    elif call.data == "tesnel":
        see_tasks(call.message, user_id)
    elif call.data == "nshel":
        bot.send_message(call.message.chat.id, "Գրեք գաղտնաբառը")
        bot.register_next_step_handler(call.message, update_task_status)

        

def get_task_text(message):
    user_id = str(message.from_user.id)
    task_data[user_id]["task"] = message.text
    bot.send_message(message.chat.id, "Հիմա մուտքագրեք task-ի գաղտնաբառը")
    bot.register_next_step_handler(message, get_task_password)

# Task-ի գաղտնաբառը ստանալ և ավելացնել տվյալների բազա
def get_task_password(message):
    user_id = str(message.from_user.id)
    task_data[user_id]["password"] = message.text

    insert = '''
        INSERT INTO tasks (telegram_id, task, task_password, procces) VALUES (%s, %s, %s, %s);
    '''
    cursor.execute(insert, (user_id, task_data[user_id]["task"], task_data[user_id]["password"], "Կատարված չէ"))
    connection.commit()

    bot.reply_to(message, "✅ Ձեր task-ը հաջողությամբ ավելացվեց!")

def delete_task(message, user_id):
    delete = '''
        DELETE FROM tasks WHERE telegram_id = (%s) AND procces = (%s);
    '''
    cursor.execute(delete, (user_id, "Կատարված է",))
    connection.commit()
    bot.reply_to(message, "Ձեր կատարված առաջադրանքները ջնջվեցին")

def see_tasks(message, user_id):
    select = '''
        SELECT * FROM tasks WHERE telegram_id = %s;
    '''
    cursor.execute(select, (user_id,))
    tasks = cursor.fetchall()

    if tasks:
        for task in tasks:
            bot.send_message(message.chat.id, f"📌 **Task**: {task[2]}\n✅ **Կարգավիճակ**: {task[5]}", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "❌ Այդ ամսաթվով task չկա")

def update_task_status(message):
    password = message.text

    update = '''
        UPDATE tasks SET procces = %s WHERE task_password = %s;
    '''
    cursor.execute(update, ("Կատարված է", password))
    connection.commit()

    bot.send_message(message.chat.id, "✅ Ձեր task-ը նշվեց որպես կատարված!")

bot.polling()