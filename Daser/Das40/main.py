import telebot
from telebot import types



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
        bot.send_message(call.message.chat.id, "Շատ լավ, ուղարկեք ձեր նկարի լինկը")
        bot.register_next_step_handler(call.message, image)

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
    user_data[user_id]["language"] = message.text
    bot.reply_to(message, "Շնորհակալություն ձեր հայտը ուղարկվեց")
    bot.send_photo(6422967638, user_data[user_id]["photo"])
    bot.send_message(6422967638,
    f"Անունը և ազգանունը։ {user_data[user_id]['name']}\n Մայլը։ {user_data[user_id]['mail']}\n Հեռախոսահամար։ {user_data[user_id]['phone']}\n Սովորելա։ {user_data[user_id]['school']}\n Լեզուներ։ {user_data[user_id]['language']}\n", parse_mode="Markdown")

bot.polling()