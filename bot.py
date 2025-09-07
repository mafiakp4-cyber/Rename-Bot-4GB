from threading import Thread
from flask import Flask
import os

from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod

# Flask dummy server
server = Flask(__name__)

@server.route('/')
def home():
    return "✅ Telegram Rename Bot is running on Render!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    server.run(host="0.0.0.0", port=port)

def run_bot():
    bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

    if STRING_SESSION:
        apps = [Client2, bot]
        for app in apps:
            app.start()
        idle()
        for app in apps:
            app.stop()
    else:
        bot.run()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    Thread(target=run_bot).start()




# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
