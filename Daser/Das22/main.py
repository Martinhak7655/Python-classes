# import telebot

# BOT_TOKEN = ""

# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=["start"])
# def start(message):
#     user_name = message.from_user.first_name
#     bot.reply_to(message, f"Hello {user_name}, Im bot. Get my id /myid")

# @bot.message_handler(commands=["myid"])
# def my_id(message):
#     user_id = message.from_user.id
#     bot.reply_to(message, f"<b><i>Your Id ➡️ {user_id}</i></b>", parse_mode="HTML")

# bot.polling()