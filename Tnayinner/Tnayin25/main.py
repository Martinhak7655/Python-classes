import telebot 
import os
import psycopg2

BOT_TOKEN = "7425549062:AAE6syBg2hklS3DytxIDDsFJpF-hTQD_uT0"
bot = telebot.TeleBot(BOT_TOKEN)

connection = psycopg2.connect(
    host="localhost",
    database="downloadimage",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        file_name TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

SAVE_FOLDER = "./downloads"
os.makedirs(SAVE_FOLDER, exist_ok=True)

@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    bot.reply_to(message, "Բարև, ուղարկիր ինձ նկար")

@bot.message_handler(content_types=["photo"])
def photo(message):
    username = message.from_user.username
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    with open(file_path, 'wb') as f:
     f.write(download_file)
    insert = '''
        INSERT INTO users (username, file_name) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, file_name,))
    connection.commit()
    bot.reply_to(message, "Նկարը քաշվեց")


bot.polling()