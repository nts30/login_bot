from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_profile = KeyboardButton('Профиль')
btn_sub = KeyboardButton('Подписка')
btn_delete = KeyboardButton('Удалить профиль')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(btn_profile, btn_sub)
main_menu.add(btn_delete)
