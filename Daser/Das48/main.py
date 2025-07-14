import telebot
import os

BOT_TOKEN = "8074746452:AAGydQnfc2GBXI026TBW3fmV7t1B7znRjCM"
bot = telebot.TeleBot(BOT_TOKEN)

AUDIO_FOLDER = "./audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Բարև, ուղարկիր ինձ աւդիո")

@bot.message_handler(content_types=["audio"])
def audio(message):
    file_info = bot.get_file(message.audio.file_id)
    download_file = bot.download_file(file_info.file_path)
    file_name = f"{message.audio.file_id}.mp3"
    file_path = os.path.join(AUDIO_FOLDER, file_name)
    with open(file_path, "wb") as f:
        f.write(download_file)

    bot.reply_to(message, "Դուք ուղարկեցիք աուդիո")

bot.polling()