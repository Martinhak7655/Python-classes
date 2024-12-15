import telebot
import requests

BOT_TOKEN = "8113612983:AAEbNmETuntpytoJxWIyZsJInsLmoEr7cCw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Enter Country Name")

@bot.message_handler(content_types=["text"])
def data(message):
    try:
        country_name = message.text

        res = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        data = res.json()
        bot.reply_to(message, f"Population: {data[0]["population"]}")
        bot.reply_to(message, f"Capital City:  {data[0]["capital"][0]}")
    except:
        print("Error")

bot.polling()