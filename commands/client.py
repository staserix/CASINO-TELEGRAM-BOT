from aiogram import types, Dispatcher
from creat import *

from asyncio import sleep
from textwrap import dedent
from aiogram.types import Message


# @dp.message_handler(commands=['spin'])
async def send_spin(message: types.Message):
    msg = await message.answer_dice(emoji="🎰")
    dice_value = msg.dice.value
    await sleep(2)

    if dice_value in (1, 22, 43):
        await bot.send_message(message.from_user.id, "Win")
    elif dice_value in (16, 32, 48):
        await bot.send_message(message.from_user.id, "Win")
    elif dice_value == 64:
        await bot.send_message(message.from_user.id, "jackpot")
    else:
        await bot.send_message(message.from_user.id, "Loss")


# @dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!")


# @dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("/dice - to play a dice")


# @dp.message_handler(commands=['dice'])
async def send_dice(message: types.Message):
    """
    This handler will be called when user sends `/dice` command
    """
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']

    await sleep(4)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Loss")

    elif bot_data == user_data:
        await bot.send_message(message.from_user.id, "Drave")
    else:
        await bot.send_message(message.from_user.id, "Win")


def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_help, commands=['help'])
    dp.register_message_handler(send_dice, commands=['dice'])
    dp.register_message_handler(send_spin, commands=['spin'])

