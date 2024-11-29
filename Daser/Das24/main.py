import telebot
from telebot import types

BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/functional")
    markup.add(btn1)
    bot.reply_to(message, "Hi! I'm Bot", reply_markup=markup)

@bot.message_handler(commands=["functional"])
def functional(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Say Hi", callback_data="say_hi")
    btn2 = types.InlineKeyboardButton("Get My Id", callback_data="get_my_id")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Choose Button", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "say_hi":
        bot.send_message(call.message.chat.id, "Hi Im Bot")
    else:
        user_id = call.from_user.id
        bot.send_message(call.message.chat.id, f"{user_id}")

bot.polling()