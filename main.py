import telebot
from telebot import types
token = "2125864106:AAFf6xw8cz32N9nOfVlBigRaz6XiBdY1fjY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Фильм", "/oscars", "/rating")
    bot.send_message(message.chat.id, 'Привет! Хочешь подберу тебе фильм? Или покажу новинки? Могу также показать информацию о церемонии оскар или список фильомов по рейтингу?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['rating'])
def rating(message):
    bot.send_message(message.chat.id, "Список фильмов по рейтингу - https://www.kinopoisk.ru/lists/top250/?tab=all")

@bot.message_handler(commands=['new'])
def new(message):
    bot.send_message(message.chat.id, "Список новинок - https://www.kinopoisk.ru/lists/navigator/2021/?quick_filters=films&tab=all ")


@bot.message_handler(commands=['oscars'])
def oscars(message):
    buttons = [
        types.InlineKeyboardButton(text="Лучшая мужская роль", callback_data="best_mrole"),
        types.InlineKeyboardButton(text="Лучшая жеснкая роль", callback_data="best_fmrole"),
        types.InlineKeyboardButton(text="Лучший фильм", callback_data="best_movie"),
        types.InlineKeyboardButton(text="Лучший режиссер", callback_data="best_director")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=7)
    keyboard.row(*buttons)
    bot.send_message(message.chat.id, 'Узнайте информацию о цермеонии оскар', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    action = call.data.split("_")[1]
    if action == "mrole":
        bot.send_message(call.message.chat.id, "https://www.kinopoisk.ru/name/8968/")
    elif action == "fmrole":
        bot.send_message(call.message.chat.id, "https://www.kinopoisk.ru/name/7222/")
    elif action == "director":
        bot.send_message(call.message.chat.id, "https://www.kinopoisk.ru/name/1734706/")
    elif action == "movie":
        bot.send_message(call.message.chat.id, "https://www.kinopoisk.ru/film/1238506/")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о мире кино?', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "Да":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row("триллер", "драма", "комедия", "мистика", "приключения", "спорт", "ужасы", "фэнтези", "исторический")
        bot.send_message(message.chat.id, 'Выбери интересующий жанр', reply_markup=keyboard)
    elif message.text == "триллер":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/361/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/930534/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/635772/")
    elif message.text == "драма":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/535341/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/448/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/41519/")
    elif message.text == "комедия":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/6039/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/507817/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/555/")
    elif message.text == "мистика":
        bot.send_message(message.chat.id, "https://www.kinonews.ru/movie_2682/the-shining")
        bot.send_message(message.chat.id, "https://www.kinonews.ru/movie_214156/irrational-man")
        bot.send_message(message.chat.id, "https://www.kinonews.ru/movie_218971/a-man-in-the-dark")
    elif message.text == "приключения":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/102124/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/7121/")
        bot.send_message(message.chat.id, "hhttps://www.kinopoisk.ru/film/339/")
    elif message.text == "спорт":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/601564/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/840817/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/596125/")
    elif message.text == "ужасы":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/453397/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/series/915196/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/1044906/")
    elif message.text == "фэнтези":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/689/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/328/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/496849/")
    elif message.text == "исторический":
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/474/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/series/682255/")
        bot.send_message(message.chat.id, "https://www.kinopoisk.ru/film/399/")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

