import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, запущенный с Render.")

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()  # Загружает токен из .env файла (для локального запуска)

    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()