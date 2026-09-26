import telebot

# Apna BotFather wala token yahan daalein
API_TOKEN = '8975665522:AAGgSX9u72TdLeET5kHLRGoF7E5ymKxduWA'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! VS Code se bot chalu ho gaya hai. Boliye kya madad karu?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot chalu ho gaya hai...")
bot.polling() 