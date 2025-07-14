import telebot
import psycopg2
import os


BOT_TOKEN = "8166197196:AAEfHREmsBWlUUVNXOjQ1V1Y56etWcbcVyg"
bot = telebot.TeleBot(BOT_TOKEN)

IMAGE_FOLDER = "./images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)


connection = psycopg2.connect(
    host="localhost",
    database="saveimage",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        image_name TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

create_table2 = '''
    CREATE TABLE IF NOT EXISTS admin(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table2)
connection.commit()

def exists_admin(username):
    select = '''
        SELECT * FROM admin WHERE username = (%s);
    '''
    cursor.execute(select, (username,))
    connection.commit()
    admin = cursor.fetchone()
    if admin:
        return True

@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.username
    admin = message.text
    if not exists_admin(username):
        bot.reply_to(message, "Բարև ուղղարկիր նկար")
    select = '''
        SELECT * FROM users WHERE username = (%s);
    '''
    cursor.execute(select, (admin,))
    connection.commit()
    users = cursor.fetchone()
    if users:
        bot.send_photo(message.chat.id, open(f"{users[2]}", "rb"))
    
@bot.message_handler(content_types=["image"])
def photo(message):
    photo = message.photo[-1]
    username = message.from_user.username
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(IMAGE_FOLDER, file_name)
    with open(file_path, "wb") as f:
        f.write(download_file)
    insert = '''
        INSERT INTO users (username, image_name) VALUES (%s, %s);
    '''
    cursor.execute(insert, (username, file_name,))
    connection.commit()


bot.polling()