import telebot
from telebot import types

bot = telebot.TeleBot("1750685032:AAHbsmhiIp9SA5d71JIA9T8fEdoLPPayq0s")

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
		bot.delete_message(message.chat.id, message.id)	
	pass


bot.polling()

while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
