import telebot
from telebot import types

BOT_TOKEN = "7701837387:AAGMgH1mzAmKWoc0rtq86uZ2lT9PwN9CTdU"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Լռացնել իմ ինքնակենսագրականը", callback_data="cv")
    markup.add(button)
    bot.reply_to(message, "Խնդրում ենք մանրամասնել ձեր մասին", reply_markup=markup)

user_data = {}
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.from_user.id
    if call.data == "cv":
        user_data[user_id] = {}
        bot.send_message(call.message.chat.id, "Շատ լավ, ուղարկեք ձեր նկար")
        bot.register_next_step_handler(call.message, image)
    elif call.data == "hastatel":
        bot.send_message(call.message.chat.id, "Խմդրում եմ գրեք հայտը ուղարկողի այդին")
        bot.register_next_step_handler(call.message, confirm_id)
    elif call.data == "merjel":
        bot.send_message(call.message.chat.id, "Խմդրում եմ գրեք հայտը ուղարկողի այդին")
        bot.register_next_step_handler(call.message, canceled_id)


def image(message):
    user_id = message.from_user.id

    photo_id = message.photo[-1].file_id
    user_data[user_id]["photo"] = photo_id

    bot.reply_to(message, "Շատ լավ, հիմա գրեք անուն ազգանուն")
    bot.register_next_step_handler(message, name_surname)

def name_surname(message):
    user_id = message.from_user.id
    user_data[user_id]["name"] = message.text
    bot.reply_to(message, "Շատ լավ, հիմա գրեք մայլ")
    bot.register_next_step_handler(message, mail)

def mail(message):
    user_id = message.from_user.id
    user_data[user_id]["mail"] = message.text
    bot.reply_to(message, "Շատ լավ, հիմա գրեք հեռախոսահամար")
    bot.register_next_step_handler(message, phone)

def phone(message):
    user_id = message.from_user.id
    user_data[user_id]["phone"] = message.text
    bot.reply_to(message, "Շատ լավ, հիմա գրեք թե որտեղ եք սովորել ծրագարավորում")
    bot.register_next_step_handler(message, school)

def school(message):
    user_id = message.from_user.id
    user_data[user_id]["school"] = message.text
    bot.reply_to(message, "Շատ լավ, հիմա գրեք թե ինչ ծրագարավորման լեզուներ գիտեք")
    bot.register_next_step_handler(message, language)

def language(message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data[user_id]["language"] = message.text
    bot.reply_to(message, "Շնորհակալություն ձեր հայտը ուղարկվեց")
    bot.send_photo(6422967638, user_data[user_id]["photo"])
    bot.send_message(6422967638,
    f"Օգտագործողի այդին։ {user_id}\n username ը։ {username}\n Անունը և ազգանունը։ {user_data[user_id]['name']}\n Մայլը։ {user_data[user_id]['mail']}\n Հեռախոսահամար։ {user_data[user_id]['phone']}\n Սովորելա։ {user_data[user_id]['school']}\n Լեզուներ։ {user_data[user_id]['language']}\n", parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Հաստատել", callback_data="hastatel")
    btn2 = types.InlineKeyboardButton("Մերժել", callback_data="merjel")
    markup.add(btn1, btn2)
    bot.send_message(6422967638, "Հաստատել թե մերժել", reply_markup=markup)

def confirm_id(message):
    user_id = int(message.text)
    bot.send_message(user_id, "Ձեր հայտը հաստատվեց")
    bot.reply_to(message, "Պատասխանը ուղարկվեց")

def canceled_id(message):
    user_id = int(message.text)
    bot.send_message(user_id, "Ձեր հայտը չեղարկվեց")
    bot.reply_to(message, "Պատասխանը ուղարկվեց")


bot.polling()