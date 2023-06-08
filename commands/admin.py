from aiogram import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from creat import *


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands=['upload'], state=None)
async def load(message: types.Message):
    """
    This handler will be called when user sends `/upload` command
    """
    await FSMAdmin.photo.set()
    await message.reply('upload a photo')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('upload a name')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('upload a description')


# @dp.message_handler(state=FSMAdmin.name)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('upload a price')


# @dp.message_handler(state=FSMAdmin.name)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    # sql_add(state)
    await state.finish()


# @dp.message_handler(state="*", commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_load(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ok')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(load, commands=["load"], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_load, state="*", commands='cancel')
    dp.register_message_handler(cancel_load, Text(equals='cancel', ignore_case=True), state="*")
