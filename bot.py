import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = "8253494296:AAGKIM5_MHqdrzEafqaf5NkYNsnC1PvktIY"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    await update.message.reply_text("🔎 Searching...")
    
    url = f"https://api.vevioz.com/api/button/mp3/{text}"
    
    await update.message.reply_text(f"🎵 Download here:\n{url}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
