from config import bot
from controller.controller import signin, signup, popoxum, jnjel
from model.model import create
from telebot import types

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    if signin(str(user_id)):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Popoxel im anuny", callback_data="popoxum")
        btn2 = types.InlineKeyboardButton("Jnjel im ejy", callback_data="jnjel")
        markup.add(btn1, btn2)
        bot.reply_to(message, "Yntreq kocakneric voreve meky", reply_markup=markup)
    elif signup(str(user_id), username):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Popoxel im anuny", callback_data="popoxum")
        btn2 = types.InlineKeyboardButton("Jnjel im ejy", callback_data="jnjel")
        markup.add(btn1, btn2)
        bot.reply_to(message, "Yntreq kocakneric voreve meky", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.from_user.id
    if call.data == "popoxum":
        bot.send_message(call.message.chat.id, "Greq popoxman entaka anuny")
        @bot.message_handler(content_types=["text"])
        def change_username(message):
            username = message.text
            popoxum(username, str(user_id))
            bot.reply_to(message, "Dzer anuny hajoxutyamb popoxvec")
    elif call.data == "jnjel":
        jnjel(str(user_id))
        bot.send_message(call.message.chat.id, "Dzer ejy hajoxutyamb jnjvec")

if __name__ == "__main__":
    create()
    bot.polling()
  