import telebot
from telebot import types

bot = telebot.TeleBot("1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es")

def del(message):
  k= message.document.mime_type;
  k=k.split("/");
  if (k[0]=="application"):
    return trure
  else:
    return false

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
  f=del(message);
  if(f==true):
    bot.deleteMessage(message.chat.id, message.id);
	pass


bot.polling()
