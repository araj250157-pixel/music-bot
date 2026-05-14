import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def download_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text("🔍 Searching...")

    try:
        # Free API (no YouTube)
        url = f"https://api.vevioz.com/api/button/mp3/{query}"
        
        await update.message.reply_text(f"🎵 Download here:\n{url}")

    except Exception as e:
        await update.message.reply_text("❌ Error: " + str(e))

# keep alive
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot running"

def run():
    app_flask.run(host='0.0.0.0', port=10000)

def keep_alive():
    Thread(target=run).start()

keep_alive()

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_song))

app.run_polling()
