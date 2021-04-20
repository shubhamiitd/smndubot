# This example show how to use inline keyboards and process button presses
import telebot
import time
import emoji
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup(tk):
    i=0
    k=[]
    while(i<len(tk)):
        k.append(InlineKeyboardButton(tk[i], callback_data=emoji.demojize(tk[i])));
        print(len(tk))
        print(k);
        i=i+1
    print([k]);
    markup = InlineKeyboardMarkup([k]);
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    kw=call.data
    k="you have"+kw+"this post";
    bot.answer_callback_query(kw, k)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    tk=message.text
    tk=tk.split('*')
    bot.send_message(message.chat.id, "post fdjfdbhj hjfdhjgbhjfg fbgdhjgbjhgbhjg fhgbdfhjgbfhdjg fjgdhjgbfdjhgbdjg gdjhgbfdjkgbdfjhgb fgbhjdbgjhdbgjhdgb fhjghjdgbhjgtext", reply_markup=gen_markup(tk))








"""

import telebot
import time

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())



@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Send us the new post. Post can contain :images, text."
    )

@bot.message_handler(content_types=["text", "image"])
def handle_text_image(message):
    tk=message.text
    tk=tk.split('*')
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in tk:
        keyboard.add(telebot.types.InlineKeyboardButton(i),url="dshfgsjh.dsfds")
    bot.send_message(message.chat.id,"post",reply_markup=keyboard)
    pass


"""

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

