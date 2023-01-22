from aiogram.types import *

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Меню"), KeyboardButton("📥 Корзина")],
        [KeyboardButton("🚖 Оформить заказ")]
    ], resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🍔 Бургер"), KeyboardButton("🌭 Хот-Дог")],
        [KeyboardButton('🍗 Куриные крылышки(острые)')],
        [KeyboardButton("🍹 Напитки"), KeyboardButton("🍟 Дополнительно")]
    ], resize_keyboard=True
)

back = KeyboardButton("⬅️ Назад")
home = KeyboardButton('Главное меню')
keypad = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(1), KeyboardButton(2), KeyboardButton(3)],
        [KeyboardButton(4), KeyboardButton(5), KeyboardButton(6)],
        [KeyboardButton(7), KeyboardButton(8), KeyboardButton(9)],
        [home, KeyboardButton('⬅️ Назад')]
    ], resize_keyboard=True
)


def cart_markup(items):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in items:
        markup.insert(KeyboardButton(f"{i[1]} x {i[-2]}"))
    markup.row(back, home)
    markup.add(KeyboardButton('Clear'))
    return markup


def pro_mark(items):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        markup.add(KeyboardButton(item[2]))
    markup.row(back, home)
    return markup


restart = ReplyKeyboardMarkup(keyboard=[["/start"]])
