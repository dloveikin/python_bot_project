from bot_config import dp, Dispatcher
from aiogram.utils import executor
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)

# future connection to database
async def on_starup(_):
    print("\033[1;32m BOT ONLINE SUCCESSFULLY")

from client import *

register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_starup)



