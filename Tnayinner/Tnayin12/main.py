import telebot

BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Welcome To Your Bot")
    bot.reply_to(message, f"Get my <b>/myid</b> or my <b>/myname</b>", parse_mode="HTML")

@bot.message_handler(commands=["myid"])
def myid(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your id → <b>{user_id}</b>", parse_mode="HTML")

@bot.message_handler(commands=["myname"])
def myname(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Your name → <b>{user_name}</b>", parse_mode="HTML")

bot.polling()