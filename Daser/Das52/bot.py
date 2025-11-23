import telebot
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9090))


BOT_TOKEN = "8542801228:AAElAXO4IQjvUicnV2qxw5xzcULHXERUW2o"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def start(message):


    bot.reply_to(message, "Hello")
    text = message.text
    client.send(text.encode())

bot.polling()