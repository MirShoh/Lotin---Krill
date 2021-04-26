from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "1404386274:AAFeYGNH-B4CwiThBAjnxJwM6B_qZblgtoA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    xabar  = "Assalomu alaykum! Xush kelibsiz! \nIstalgan matnni kiriting: "
    bot.reply_to(message, xabar)

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
        
    bot.reply_to(message, javob(msg))
    
bot.polling()

# matn = input("So'zni kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))