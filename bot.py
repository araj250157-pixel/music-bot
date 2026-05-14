import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import yt_dlp
from flask import Flask
from threading import Thread

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def download_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text("🔍 Searching...")

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch',
        'nocheckcertificate': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=True)
            entry = info['entries'][0]
            file_name = ydl.prepare_filename(entry)

        await update.message.reply_audio(audio=open(file_name, 'rb'))

    except Exception as e:
        await update.message.reply_text("❌ Error:\n" + str(e))

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
