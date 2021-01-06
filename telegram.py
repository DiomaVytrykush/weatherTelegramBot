import telebot
from pyowm import OWM
from pyowm.utils import config

bot = telebot.TeleBot("1559052754:AAEZYwu8joUxblzQonxw1ORlZDgEAa71dg4")

owm = OWM('07e20f6937696b2ce446691631840639')
mgr = owm.weather_manager()


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    weather = observation.weather
    temp = round(weather.temperature('celsius')["temp"])

    answer = "In " + message.text + " now " + weather.detailed_status + "\n"
    answer += "Temperature now: " + str(temp) + "°C" + "\n\n"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
