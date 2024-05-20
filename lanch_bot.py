# launch_bot

# region Импорты
import telebot
from config import *
from methods import generate_help_message
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from game.rock_and_paper import game

# endregion

bot = telebot.TeleBot(TOKEN)


# region Комманды
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую я бот')


@bot.message_handler(commands=['help'])
def help(message):
    help_message = generate_help_message()
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['game'])
def chose_game(message):
    markap = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    markap.add(KeyboardButton("Камень, ножницы, бумага"))
    bot.send_message(chat_id=message.chat.id, text="Выберите игру", reply_markup=markap)


# endregion
# region Работа с текстом
@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == "Камень, ножницы, бумага":
        markap = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        markap.add(KeyboardButton("камень"))
        markap.add(KeyboardButton("ножницы"))
        markap.add(KeyboardButton("бумага"))
        bot.send_message(chat_id=message.chat.id, text="Выберите знак", reply_markup=markap)
        bot.register_next_step_handler(message, rock_and_paper_game)
    else:
        bot.send_message(message.chat.id, text=f"'{message.text}' Не входит в список команд")
        help(message)


# endregion
def rock_and_paper_game(message):
    game_res = game(message)
    bot.send_message(message.chat.id, game_res[0])
    if game_res[1]:
        chose_game(message)
    else:
        bot.send_message(chat_id=message.chat.id, text="Еще один раунд")
        markap = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        markap.add(KeyboardButton("камень"))
        markap.add(KeyboardButton("ножницы"))
        markap.add(KeyboardButton("бумага"))
        bot.send_message(chat_id=message.chat.id, text="Выберите знак", reply_markup=markap)
        bot.register_next_step_handler(message, rock_and_paper_game)


if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling(none_stop=True)
