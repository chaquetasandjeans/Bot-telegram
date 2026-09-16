import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

web_app = Flask(__name__)
@web_app.route('/')
def home():
    return "Bot chaquetas activo"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Bienvenido a Chaquetas y Vaqueros 🧥 Dime que talla buscas?")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot iniciado...")
app.run_polling()
