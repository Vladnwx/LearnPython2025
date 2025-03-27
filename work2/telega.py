import telebot
from openweathermap import get_openweathermap_temp, get_openweathermap_temp_feelds
from secret import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
# приветственный текст
start_txt = "Привет! Это бот прогноза погоды. \nОтправь боту название города и он скажет какая температура и как она ощущается"


# обрабатываем старт бота
@bot.message_handler(commands=["start"])
def defstart(message):
    # выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode="Markdown")


# обрабатываем полученное сообщение(город)
@bot.message_handler(content_types=["text"])
def defweather(message):
    # получаем город из сообщения пользователя
    city = message.text.strip()
    # отправляем запрос на сервер
    # получаем данные о температуре и том, как она ощущается
    try:
        temperature = get_openweathermap_temp(city)
        temperature_feels = get_openweathermap_temp_feelds(city)
        # формируем ответы
        w_now = "Сейчас в городе " + city +" "+ str(temperature) + " °C"
        w_feels = "Ощущается как " + " " + str(temperature_feels) + " °C"
        # отправляем значения пользователю
        bot.send_message(message.chat.id, w_now)
        bot.send_message(message.chat.id, w_feels)
    except Exception as e:
        error_message = f"Не удалось получить погоду для города '{city}'.\n"
        bot.send_message(message.chat.id, error_message)
        print(f"Ошибка при запросе погоды: {e}")


# запускаем бота
if __name__ == "__main__":
    while True:
        # в бесконечном цикле постоянно опрашиваем бота есть ли новые сообщения
        try:
            bot.polling(none_stop=True, interval=0)
            # если возникла ошибка — сообщаем про исключение и продолжаем работу
        except Exception as e:
            print("❌❌❌❌❌ Сработало исключение!  ❌❌❌❌❌")
