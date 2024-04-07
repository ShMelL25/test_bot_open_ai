from aiogram import types, F, Router, flags, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer('Hello')