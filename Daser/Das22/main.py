import telebot
import random

BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

sticker_answer = ["Good Sticker!", "Perfeckt", "Good"]
image_aswer = ["Good image!", "Beautiful image!", "good"]

@bot.message_handler(commands=["start"])
def start(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Hello {user_name}, Im bot. Get my id /myid")

@bot.message_handler(commands=["myid"])
def my_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"<b><i>Your Id ➡️ {user_id}</i></b>", parse_mode="HTML")

@bot.message_handler(content_types=["sticker"])
def sticker(message):
    sticker_random = random.randint(0, len(sticker_answer) - 1)
    bot.reply_to(message, sticker_answer[sticker_random])

@bot.message_handler(content_types=["photo"])
def image(message):
    image_random = random.randint(0, len(image_aswer) - 1)
    bot.reply_to(message, image_aswer[image_random])

bot.polling()