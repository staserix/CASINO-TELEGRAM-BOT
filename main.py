import logging

from aiogram import executor

from creat import dp
from commands import client, admin, other

# Configure logging
logging.basicConfig(level=logging.INFO)

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
