# This example show how to use inline keyboards and process button presses
import telebot
import time
import emoji
import mysql.connector
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '1607683994:AAGotYV7rp5cixLimS33rr0P1ir3-BBm6es'
db = mysql.connector.connect(host="localhost",user="root",password="you",database="smndubot")

cursor = db.cursor()

bot = telebot.TeleBot(TELEGRAM_TOKEN)
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Welcome to SmndUnibot. \n To use this bot the following commands \:\n newpost = create a new post. \n /editpost = edit a post.\nThis bot accepts only text and images in the post."
        )

def reply(message,update_id):
    sender_id=message.from_user.id
    username=message.chat.username
    message_id=message.message_id
    chat_id=message.chat.id
    first_name=message.chat.first_name
    text=message.text
    update_id=update_id
    if "photo" in message["message"]:
        attachments=1
        attachments_id=message.photo.file_unique_id
        #save photo to directory
        dir="img/"+attachments_id+".jpg"
        file_info = bot.get_file(message.photo.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TELEGRAM_TOKEN, file_info))
        with open(dir, 'wb') as f:
            f.write(file.content)
    else:
        attachments=0
        attachments_id=""
    
    #save to db
    sql = """INSERT INTO messages(sender_id, sender_name, sender_username, message_id, chat_id, text, attachments, attachments_id, update_id)VALUES (sender_id,username, message_id,chat_id, text,attachments, attachments_id,update_id)"""
    cursor.execute(sql)
    mydb.commit()
    markup="Now please send us the reaction button emojis separated by (*) Eg:😍*🥳*💕 will create three buttons for you. You may add max of 6 buttons. If you want to edit the above post, type : /editpost. "
    return (markup)
    

    
@bot.message_handler(commands=["newpost"])
def send_welcome1(message,update_id):
    bot.send_message(message.chat.id, "Create a new post. Your post can contain images or text.",reply_markup=reply(message,update_id))
        
@bot.message_handler(commands=["editpost"])
def send_welcome2(message):
    bot.send_message(
        message.chat.id, "This will be added soon."
        )


def gen_markup(tk):
    i=0
    k=[]
    while(i<len(tk)):
        k.append(InlineKeyboardButton(tk[i], callback_data=tk[i]));
        i=i+1
    print([k]);
    markup = InlineKeyboardMarkup([k]);
    return markup

@bot.message_handler(func=lambda message: True)
def message_handler(message,update_id):
    #db check updateid-1
    sql="select * from messages where sender_id="+str(message.from_user.id)+" AND update_id= "+str(update_id-1)
    cursor.execute(sql)
    records= cursor.fetchall()
    
    if (len(records!=0)):
        attachment=records[0][6]
        photo=records[0][7]
        caption=records[0][5]
        tk=message.text
        tk=tk.split('*')
        if (attachment==0):
            bot.send_message(message.chat.id, caption, reply_markup=gen_markup(tk))
        else:
            bot.sendPhoto(message.chat.id, photo, caption = caption, reply_markup=gen_markup(tk))
    else:
        bot.send_message(message.chat.id, "The above message can't be recognised. Please follow the guidelines.")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    kw=call.data
    print(kw);
    k="you have "+kw+" this post."
    print(k);
    bot.answer_callback_query(call.id, k)
    pass







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
