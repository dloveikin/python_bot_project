from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/help")
b2 = KeyboardButton("/back")
b3 = KeyboardButton("/next")
b4 = KeyboardButton("/edit")

kb_cl = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cl = ReplyKeyboardMarkup(resize_keyboard=True)

kb_cl.add(b1).row(b2, b3).add(b4)
# .add - add new line with buttin
# .row(b1, ... ,b_n) - add line
# .insert(b1) - add new button in line