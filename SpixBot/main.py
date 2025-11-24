import telebot
import random
import os

bot = telebot.TeleBot("8577051329:AAHJLGR5RorHUTUM6E_17Vm82EJGSSmLK0g")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот SpixStandUpBot. Чем могу помочь?")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Доступные команды: /start /help /fnoy /arts /random_art")

@bot.message_handler(commands=['arts'])
def send_arts(message):
    img_list = [
        'images/офис.png',
        'images/чел для игры.png',
        'images/ssc.png',
        'images/T2X2_BIG.png',
        'images/Tvich.png',
        'images/youtube без стрингов.png'
    ]

    media = []
    for img_path in img_list:
        media.append(telebot.types.InputMediaPhoto(open(img_path, 'rb')))

    bot.send_media_group(message.chat.id, media)



@bot.message_handler(commands=['random_art'])
def send_rand_arts(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

bot.polling()