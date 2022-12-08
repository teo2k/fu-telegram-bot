import telebot
bot = telebot.TeleBot('5820580999:AAEl6HI68CTWPhkSCExCZbN_3sJ13UQieTc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! К сожалению в данный момент ведутся технические работы над ботом. Попробуй чуть позже.".format(
                         message.from_user))
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == ""):
        bot.send_message(message.chat.id, text="Попробуйте чуть позже")
    else:
        bot.send_message(message.chat.id, text="Попробуйте чуть позже")