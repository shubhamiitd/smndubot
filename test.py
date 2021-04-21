
import telebot
from telebot import types

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")

@bot.callback_query_handler(func=lambda callback: True)
def callbacks(callback):
    new_keyboard = types.InlineKeyboardMarkup()
    new_keys = []
    for button in callback.message.reply_markup.keyboard[0]:
        text = button.text
        callback_data = button.callback_data
        if callback_data == callback.data:
            if len(button.text) == 1:
                text = text+" 1"
            else:
                count = text[2:]
                text = text.replace(count, str(int(count)+1))
        new_button = types.InlineKeyboardButton(text=text, callback_data=callback_data)
        new_keys.append(new_button)
    new_keyboard.add(*new_keys)
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=new_keyboard)

@bot.message_handler(commands=['start'])
def start_func(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="👍", callback_data="test")
    button2 = types.InlineKeyboardButton(text="😍", callback_data="test2")
    keys = [button1, button2]
    keyboard.add(*keys)
    bot.send_message(message.from_user.id, "Hello", reply_markup=keyboard)

bot.polling()
