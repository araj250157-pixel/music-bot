from telegram.ext import Updater, MessageHandler, Filters
import yt_dlp

BOT_TOKEN = "8253494296:AAGKIM5_MHqdrzEafqaf5NkYNsnC1PvktIY"

def handler(update, context):
    query = update.message.text
    update.message.reply_text("🔍 Searching...")

    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            url = info['entries'][0]['url']

        # direct audio bhejna
        update.message.reply_audio(url)

    except Exception as e:
        update.message.reply_text("❌ Error: " + str(e))


updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handler))

updater.start_polling()
updater.idle()
