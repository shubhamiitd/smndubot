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
    tk=message.text
    tk=tk.split('*')
    bot.send_message(message.chat.id, tk[0])
    print(tk)
    print(message.chat.id)
    pass




while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

