from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from flask import Flask

# Flask object banaya
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot is alive!"

pyrogram.utils.MIN_CHAT_ID = -1002051194704
pyrogram.utils.MIN_CHANNEL_ID = -1002051194704

bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

if STRING_SESSION:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
else:
    bot.start()
    idle()

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
