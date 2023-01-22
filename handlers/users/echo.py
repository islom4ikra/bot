from aiogram import types
from loader import dp
from keyboards.default.main import main_menu,menu

# @dp.message_handler(state="*")
# async def categories(messgae:types.Message):
#     await messgae.answer('Categoriya tanlang',reply_markup=main_menu)