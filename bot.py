import os
from flask import Flask
from threading import Thread

TOKEN = "8253494296:AAGKIM5_MHqdrzEafqaf5NkYNsnC1PvktIY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    text = """
🎵 Welcome To Music Bot

📥 Send any song name
and I will send the music.
"""

    bot.reply_to(message, text)

@bot.message_handler(func=lambda m: True)
def music(message):

    query = message.text

    msg = bot.reply_to(
        message,
        "🔍 Searching..."
    )

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                f"ytsearch1:{query}",
                download=True
            )

            file = ydl.prepare_filename(
                info['entries'][0]
            )

        audio = open(file, 'rb')

        bot.send_audio(
            message.chat.id,
            audio,
            title=query
        )

        audio.close()

        os.remove(file)

        bot.delete_message(
            message.chat.id,
            msg.message_id
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

print("Bot Running...")
bot.infinity_polling()
