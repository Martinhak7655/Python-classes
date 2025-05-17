import telebot
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="groupproject",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        telegram_id VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        points INTEGER DEFAULT 0,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

BOT_TOKEN = "8072260781:AAGyXi8AxyKt6jMUiK-HHXFBsAo45e4I46A"
bot = telebot.TeleBot(BOT_TOKEN)

def exists_user(telegram_id):
    select = '''
        SELECT * FROM users WHERE telegram_id = (%s);
    '''
    cursor.execute(select, (telegram_id,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return True
    
def add_user(telegram_id, username):
    insert = '''
        INSERT INTO users (telegram_id, username) VALUES (%s, %s);
    '''
    cursor.execute(insert, (telegram_id, username,))
    connection.commit()

@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username
    if exists_user(user_id):
        bot.send_message(-1002501638022, "Բարև Բոլորին!, ձեզ գրում է խմբի օգնող բոտը։ Եթե դուք գրեք /points ապա կստանաք թե քանի բառ էք հավաքել")
    else:
        add_user(user_id, username)
        bot.send_message(-1002501638022, "Բարև Բոլորին!, ձեզ գրում է խմբի օգնող բոտը։ Եթե դուք գրեք /points ապա կստանաք թե քանի բառ էք հավաքել")

@bot.message_handler(commands=["points"])
def get_points(message):
    print(message)
    username = message.from_user.username
    user_id = str(message.from_user.id)
    select = '''
        SELECT * FROM users WHERE telegram_id = (%s);
    '''
    cursor.execute(select, (user_id,))
    connection.commit()
    points = cursor.fetchone()
    bot.send_message(-1002501638022, f"{username} ձեր հավաքած բառը կազմում է {points[3]}")

@bot.message_handler(content_types=["text"])
def points(message):
    user_id = str(message.from_user.id)
    update = '''
        UPDATE users SET points = points + 1 WHERE telegram_id = (%s);
    '''
    cursor.execute(update, (user_id,))
    connection.commit()

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(-1002501638022, "Hello!")

# @bot.message_handler(content_types=["photo"])
# def photo(message):
#     user_id = message.from_user.id
#     message_id = message.message_id
#     print(message)
#     bot.send_message(-1002501638022, "Նկար ուղարկել չի կարելի!")

#     # bot.ban_chat_member(chat_id=-1002501638022, user_id=user_id)
#     bot.delete_message(chat_id=-1002501638022, message_id=message_id)

# @bot.message_handler(content_types=["text"])
# def text(message):
#     message_id = message.message_id
#     if message.text == "barev":
#         bot.delete_message(chat_id=-1002501638022, message_id=message_id)



bot.polling()