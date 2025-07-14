import telebot
import os

BOT_TOKEN = "7773434340:AAFlDYfMR5t2eJ70HVlfeO53QCLMJmJ9En8"
bot = telebot.TeleBot(BOT_TOKEN)

SAVE_FOLDER = "./downloads"
os.makedirs(SAVE_FOLDER, exist_ok=True)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Բարև!, ուղարկիր ինձ նկար")

@bot.message_handler(content_types=["photo"])
def download_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{photo.file_id}.jpg"
    file_path = os.path.join(SAVE_FOLDER, file_name)
    with open(file_path, 'wb') as f:
     f.write(download_file)
    bot.reply_to(message, "Նկարը քաշվեց")

bot.polling()