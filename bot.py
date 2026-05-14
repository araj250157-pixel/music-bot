from telegram.ext import Updater, MessageHandler, Filters
import yt_dlp

BOT_TOKEN = "8253494296:AAGKIM5_MHqdrzEafqaf5NkYNsnC1PvktIY"

def download_song(update, context):
    query = update.message.text
    update.message.reply_text("🔍 Searching...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            file_name = ydl.prepare_filename(info['entries'][0])

        update.message.reply_audio(open(file_name, 'rb'))

    except Exception as e:
        update.message.reply_text("❌ Error: " + str(e))


updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_song))

updater.start_polling()
updater.idle()
