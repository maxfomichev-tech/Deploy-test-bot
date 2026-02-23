import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import logging

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Логи
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Бот работает через Webhook!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Webhook настройки
WEBHOOK_URL = "https://deploy-test-bot.onrender.com/"  # URL твоего Render сервиса
PORT = int(os.environ.get("PORT", "10000"))   # Render задаёт порт через переменную окружения

# Запуск webhook
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path=TOKEN,  # URL-часть для безопасности
    webhook_url=f"{WEBHOOK_URL}{TOKEN}"
)