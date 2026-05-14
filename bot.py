from telegram.ext import Updater, MessageHandler, Filters
import requests

BOT_TOKEN = "8253494296:AAGKIM5_MHqdrzEafqaf5NkYNsnC1PvktIY"

def handle_message(update, context):
    query = update.message.text

    update.message.reply_text("🔍 Searching...")

    try:
        url = f"https://api.vevioz.com/api/button/mp3/{query}"

        r = requests.get(url)

        with open("song.mp3", "wb") as f:
            f.write(r.content)

        update.message.reply_audio(open("song.mp3", "rb"))

    except Exception as e:
        update.message.reply_text("Error: " + str(e))


updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
