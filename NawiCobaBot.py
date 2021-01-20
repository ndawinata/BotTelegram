import telebot
import datetime

bot = telebot.TeleBot("1515221232:AAGOTsYV2YXQTJ2YqsLPIoXZr-gJD2htyc4")

@bot.message_handler(commands=['start'])
def start(msg):
    nama = msg.from_user.first_name
    date = datetime.datetime.fromtimestamp(msg.date).strftime('%H:%M')
    bot.reply_to(msg, f'Hello apa kabar {nama} !, terkirim pukul {date}')

# kata yang match menggunakan regex
# @bot.message_handler(regexp='nawi')
# def text(msg):
#     bot.reply_to(msg, f'Ini adalah nama bot kami !')

# mengenali teks 
# @bot.message_handler(content_types=['text'])
# def text(msg):
#     nama = msg.from_user.first_name
#     bot.reply_to(msg, f'Hello {nama} !, ini adalah teks')

# mengenali photo
@bot.message_handler(content_types=['photo'])
def photo(msg):
    nama = msg.from_user.first_name
    bot.reply_to(msg, f'Ini adalah Photo, {nama} !')

# kirim pesan tanpa mereply
@bot.message_handler(commands=['message'])
def start(msg):
    chatid = msg.chat.id
    nama = msg.from_user.first_name
    date = datetime.datetime.fromtimestamp(msg.date).strftime('%H:%M')
    bot.send_message(chatid, f'Hello apa kabar {nama} !, terkirim pukul {date}')

# kirim gambar
@bot.message_handler(commands=['gambar'])
def text(msg):
    chatid = msg.chat.id
    bot.send_photo(chatid, open('./gambar.jpg', 'rb'))

# kirim video
@bot.message_handler(commands=['video'])
def text(msg):
    chatid = msg.chat.id
    bot.send_video(chatid, open('./videoplayback.mp4', 'rb'))

# kirim audio
@bot.message_handler(commands=['terpesona'])
def text(msg):
    chatid = msg.chat.id
    bot.send_audio(chatid, open('./terpesona.mp3', 'rb'))

# kirim file
@bot.message_handler(commands=['undangan'])
def text(msg):
    chatid = msg.chat.id
    bot.send_document(chatid, open('./undangan.pdf', 'rb'))


print('Bot is Running !')
bot.polling()
print('Bot is Terminated !')