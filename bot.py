import asyncio
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from flask import Flask
import threading
import os

# Flask app (Render ko port bind karne ke liye)
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot is running fine on Render!"

def run_web():
    port = int(os.environ.get("PORT", 5000))
    app_web.run(host="0.0.0.0", port=port)

# Start Flask in background
threading.Thread(target=run_web).start()

pyrogram.utils.MIN_CHAT_ID = -1002051194704
pyrogram.utils.MIN_CHANNEL_ID = -1002051194704

bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)

async def main():
    if STRING_SESSION:
        apps = [Client2, bot]
        for app in apps:
            await app.start()
        await idle()
        for app in apps:
            await app.stop()
    else:
        await bot.start()
        await idle()
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
