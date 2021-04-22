import telebot
from telebot import types

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")

def deletemsg(message):
	k= message.document.mime_type
	k=k.split("/")
	if (k[0]=="application"):
		return True
	else:
		return False

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document'])
def handle_docs(message):
	f=deletemsg(message)
	if(f==True):
		bot.deleteMessage(message.chat.id, message.id)	
	pass


bot.polling()

while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
