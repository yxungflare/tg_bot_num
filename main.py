from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, message

from config import TOKEN_API

HELP_COMMAND = """
Добрый день!
Бот предназначен для сложения и вычитания одного числа с самим собой.
Для начала напишите число, над которым будут выполняться операции.
Затем выберете интересующую вас операцию и получите ответ...
*Бот выполняет оперции над числом, которое ввел пользователь..."""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


inline_btn_1 = InlineKeyboardButton('+', callback_data='plus')
inline_btn_2 = InlineKeyboardButton('-', callback_data='minus')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).insert(inline_btn_2)


async def on_startup(_):
    print("Бот успешно запущен...")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Приступим! Напишите интересующее вас число...")
    await message.delete()


@dp.message_handler()
async def write_num(message: types.Message):
    if int(message.text):
        await message.answer(message.text, reply_markup=inline_kb1)


@dp.callback_query_handler(text='plus')
async def callback_write_op(callback: types.CallbackQuery):
    await callback.message.answer(str(int(callback.message.text) + 1), reply_markup=inline_kb1)


@dp.callback_query_handler(text='minus')
async def callback_write_op(callback: types.CallbackQuery):
    await callback.message.answer(str(int(callback.message.text) - 1), reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
