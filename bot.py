import telebot
token = "7805387290:AAEgkyngNsQXs5ZvK3dGXbyNDY2cFCQMd3o"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hello everyone, welcome !")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "Hello, what help do you need ?")

@bot.message_handler(func= lambda message: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        message.text)

print("bot started ✅")






bot.polling()
