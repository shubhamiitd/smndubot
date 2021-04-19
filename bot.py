import telebot 
import time

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
