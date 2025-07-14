import telebot
import os

BOT_TOKEN = "7862997606:AAGsZXqOGGxj7aG8g6u9lMjJmgH8aNGo8L0"
bot = telebot.TeleBot(BOT_TOKEN)

SAVE_FOLDER = "./downloads2"
os.makedirs(SAVE_FOLDER, exist_ok=True)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Բարև, ուղարկիր ինձ նկար")

@bot.message_handler(content_types=["photo"])
def photo(message):
    message_id = message.message_id
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    with open(file_path, 'wb') as f:
        f.write(download_file) 
    bot.delete_message(chat_id=-1002576542375, message_id=message_id)

bot.polling()

