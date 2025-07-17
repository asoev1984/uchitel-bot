
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(
    KeyboardButton("📘 Нақшаҳо"),
    KeyboardButton("📄 Фармонҳо"),
    KeyboardButton("📝 Протоколҳо"),
    KeyboardButton("🗂️ Санадҳо"),
    KeyboardButton("📚 Нақшаи яксоата (Конспект)"),
    KeyboardButton("📖 Китобҳо"),
    KeyboardButton("🎓 Аёниятҳо"),
    KeyboardButton("📑 Дастурамалҳо"),
    KeyboardButton("📊 Гузоришҳо"),
    KeyboardButton("📅 Ҷадвалҳо"),
    KeyboardButton("🧾 Маводҳои дигар"),
    KeyboardButton("🔍 Поиск")
)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("📂 МЕНЮИ АСОСӢ", reply_markup=menu_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
