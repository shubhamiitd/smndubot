import telebot
import time

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Send us the new post. Post can contain :images, text."
    )


@bot.message_handler(content_types=["text", "image"])
def handle_text_image(message):
    bot.send_message(message.chat.id, message.text)
    print(message.chat.id)
    pass


@bot.message_handler(content_types=["text", "image"])
def handle_text_image(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Message the developer", url="telegram.me/artiomtb"
        )
    )
    bot.send_message(
        message.chat.id,
        "1) To receive a list of available currencies press /exchange.\n"
        + "2) Click on the currency you are interested in.\n"
        + "3) You will receive a message containing information regarding the source and the target currencies, "
        + "buying rates and selling rates.\n"
        + "4) Click “Update” to receive the current information regarding the request. "
        + "The bot will also show the difference between the previous and the current exchange rates.\n"
        + "5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.",
        reply_markup=keyboard,
    )


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

