import telebot
import psycopg2
import random

random_numbers = {}
user_attempts = {}

BOT_TOKEN = "7840808695:AAGX-luFAJYBaLKKaki0dIfJHdJivRnXolA"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="quizizbot",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        tg_id VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        points INTEGER DEFAULT 0,
        defeat INTEGER DEFAULT 0,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

def get_random_number(length):
    number = ''
    for i in range(length):
        number += str(random.randint(0, 9))
    return number

def feedback(random_number, user_input):
    number_in = 0
    number_in_place = 0

    if user_input == random_number:
        return "Ճիշտ եք գուշակել", True
    for i in range(len(user_input)):
        if user_input[i] == random_number[i]:
            number_in_place += 1
        if user_input[i] in random_number:
            number_in += 1
    return f"Թիվը գոյություն ունի: {number_in} անգամ, թիվը իր տեղում է: {number_in_place} անգամ", False

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
    print(tg_id)
    cursor.execute(insert, (tg_id, username,))
    connection.commit()

@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.username
    tg_id = str(message.from_user.id)
    if not exists_user(tg_id):
        add_user(tg_id, username)
    number = get_random_number(5)
    random_numbers[tg_id] = number
    user_attempts[tg_id] = 10
    bot.reply_to(message, f"Բարի գալուստ, փորձեք գուշակել թիվը, ձեզ մնաց {user_attempts[tg_id]} փորձ։ Սեղմեք /points ձեր միավորները տեսնելու համար")

@bot.message_handler(commands=["points"])
def points(message):
    tg_id = str(message.from_user.id)
    select = '''
        SELECT * FROM users WHERE tg_id = (%s);
    '''
    cursor.execute(select, (tg_id,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        bot.reply_to(message, f"Դուք հաղթելեք {user[3]} անգամ, իսկ պարտվել {user[4]} անգամ")

@bot.message_handler(content_types=["text"])
def number(message):
    user_input = message.text
    tg_id = str(message.from_user.id)

    random_number = random_numbers[tg_id]
    feedback_text, is_correct = feedback(random_number, user_input)
    bot.reply_to(message, feedback_text)

    if is_correct:
        update = '''
            UPDATE users SET points = points + 1 WHERE tg_id = (%s);
        '''
        cursor.execute(update, (tg_id,))
        connection.commit()
        del random_numbers[tg_id]
        del user_attempts[tg_id]
        return


    user_attempts[tg_id] -= 1
    
    if user_attempts[tg_id] <= 0:
        bot.reply_to(message, "Ցավում եմ դուք պարտվեցիք")
        update = '''
            UPDATE users SET defeat = defeat + 1 WHERE tg_id = (%s);
        '''
        cursor.execute(update, (tg_id,))
        connection.commit()
        del random_numbers[tg_id]
        del user_attempts[tg_id]

bot.polling()