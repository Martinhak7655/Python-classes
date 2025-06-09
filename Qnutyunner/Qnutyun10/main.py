import telebot
import psycopg2
import random

random_numbers = {}
user_attempts = {}

BOT_TOKEN = "7595325669:AAGk2vB4fE0I4Udfed1ma1HuMASGZYwSCoM"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="hackgame",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        tg_id VARCHAR(100) NOT NULL,
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

def exists_user(tg_id):
    select = '''
        SELECT * FROM users WHERE tg_id = (%s);
    '''
    cursor.execute(select, (tg_id,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return True
    
def add_user(username, tg_id):
    insert = '''
        INSERT INTO users (username, tg_id) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, tg_id,))
    connection.commit()

def feedback(random_number, user_input):
    number_in = 0
    number_in_places = 0

    if user_input == random_number:
        return "Թիվը Ճիշտ եք գուշակել", True
    for i in range(len(random_number)):
        if user_input[i] == random_number[i]:
            number_in_places += 1
        if user_input[i] in random_number:
            number_in += 1
    return f"{number_in} թիվ կա գաղտնի կոդում, իսկ {number_in_places} թիվ իր տեղում է", False


@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.username
    tg_id = str(message.from_user.id)
    if not exists_user(tg_id):
        add_user(username, tg_id)
    number = get_random_number(5)
    random_numbers[tg_id] = number
    user_attempts[tg_id] = 10
    bot.reply_to(message, f"Բարի գալուստ, փորձեք գուշակել թիվը, ձեզ մնացելե {user_attempts[tg_id]} փորձ։ Ձեր միավորները տեսնելու համար սեղմեք /points ի վրա")

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
        bot.reply_to(message, f"Դուք խաղը անցելեք {user[3]} անգամ, իսկ պարտվել {user[4]} անգամ")

@bot.message_handler(content_types=["text"])
def game(message):
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
        random_numbers.clear()

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
