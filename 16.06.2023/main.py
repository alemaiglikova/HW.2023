import telebot
from telebot import types
import json

bot = telebot.TeleBot('5991756610:AAHkUmunya6wZFvpEg_q0zYmxLD7m69I4Ck')

books = []


@bot.message_handler(commands=['start'])
def start(message):
    try:
        first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь посмотреть список книг?"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Показать список книг", callback_data="show_books"))
        bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
    except Exception as error:
        print("error: ", error)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    try:
        if function_call.message:
            if function_call.data == "show_books":
                if not books:
                    bot.send_message(function_call.message.chat.id, "Список книг пуст.")
                else:
                    book_list = "<b>Список книг:</b>\n\n"
                    for book in books:
                        book_list += f"<b>Название:</b> {book['title']}\n<b>Автор:</b> {book['author']}\n\n"
                    bot.send_message(function_call.message.chat.id, book_list, parse_mode='html')
            else:
                bot.answer_callback_query(function_call.id)
    except Exception as error:
        print("error: ", error)


@bot.message_handler(commands=['publish'])
def publish(message):
    try:
        bot.send_message(message.chat.id, "Введите название книги: ")
        bot.register_next_step_handler(message, add_book_title)
    except Exception as error:
        print("error: ", error)


def add_book_title(message: telebot.types.Message):
    try:
        book_title = message.text
        bot.send_message(message.chat.id, "Введите автора книги: ")
        bot.register_next_step_handler(message, add_book_author, book_title)
    except Exception as error:
        print("error: ", error)


def add_book_author(message: telebot.types.Message, book_title):
    try:
        book_author = message.text
        book = {
            "title": book_title,
            "author": book_author
        }
        books.append(book)
        bot.send_message(message.chat.id, "Книга успешно опубликована!")
    except Exception as error:
        print("error: ", error)


if __name__ == "__main__":
    print("bot started...")
    try:
        bot.infinity_polling()
    except Exception as error:
        print("error: ", error)
    print("bot stopped...")
