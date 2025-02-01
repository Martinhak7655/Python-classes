import telebot
import requests

BOT_TOKEN = "7711590272:AAGyzTozq1st8s_HkvvjPySVxTI_KDw6aMk"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Enter Country Name")

@bot.message_handler(content_types=["text"])
def flag(message):
    try:
        flag_name = message.text
        res = requests.get(f"https://restcountries.com/v3.1/name/{flag_name}")
        data = res.json()
        bot.send_photo(message.chat.id, f"{data[0]["flags"]["png"]}")
    except:
        print("Error")

bot.polling()