from aiogram import types, Dispatcher
from App.bot_config import dp, bot
from bot_keyboard.client_keyboards import kb_cl

async def command_start(message: types.Message):
    sending_message = f'''
    Привіт <b>{message.from_user.first_name} {message.from_user.last_name}!</b>\n
Я бот який допоможе тобі оформити твоє резюме.
Твоє резюме буде складатися з данних, які ми з'ясуємо під час опитування.\n
Після оптування готовий файл з ремюме можна буде завантажити.'''
    await bot.send_message(message.chat.id, sending_message, parse_mode="html", reply_markup=kb_cl)




# Виклик функцій кліенту handlers
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])


# @dp.message_handler()
# async def command_info(message):
#     sticker_id = message.sticker.file_id
#     await bot.send_message(message.chat.id, sticker_id)

# @dp.message_handler()
# async def echo_test(message: types.Message):
#     await message.answer(message.text)
#     await message.reply(message.text)
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)