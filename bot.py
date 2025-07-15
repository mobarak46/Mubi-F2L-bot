# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Clone Code Credit : YT - @Tech_VJ / TG - @VJ_Bots / GitHub - @VJBots

import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client, idle 
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from plugins import web_server

from TechVJ.bot import TechVJBot
from TechVJ.util.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇꜱ", url="https://t.me/MUBIBOTz"),
            InlineKeyboardButton("⚡ Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+PtDbTyuIU5g3ZWY1")
        ],
        [
            InlineKeyboardButton("⚙️ Hᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("📡 Aʙᴏᴜᴛ", callback_data="about")
        ]
    ])

    await message.reply_photo(
        photo="https://graph.org/file/c68e8b426395c411d1367-f4608594f3f2e5b254.jpg https://graph.org/file/1b8060b43bd20a84489ae-796fb29839ec4ed04b.jpg",  # Replace with your image if needed
        caption=(
            "👋 Welcome {},!\n\n"
            "I am an advanced bot designed to convert files into links and shorten links for files up to 4GB. "
            "To generate a permanent download and streaming link, just upload any file.\n\n"
            "⚠️ *Note:* Sending NSFW or explicit content will lead to permanent ban.\n\n"
            "Let's begin sharing files fast and efficiently! 🚀"
        ),
        reply_markup=buttons
)

ppath = "plugins/*.py"
files = glob.glob(ppath)
TechVJBot.start()
loop = asyncio.get_event_loop()


async def start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await TechVJBot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Tech VJ Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    me = await TechVJBot.get_me()
    temp.BOT = TechVJBot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    from datetime import datetime, date
import pytz

async def start():
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    current_time = now.strftime("%H:%M:%S %p")

        # OLD (remove or comment)
# await TechVJBot.send_message(
#     chat_id=LOG_CHANNEL,
#     text=script.RESTART_TXT.format(today, current_time, "Render Deploy")
# )

# NEW – private DM to admin
await TechVJBot.send_message(
    chat_id=ADMIN_ID,
    text=script.RESTART_TXT.format(today, current_time, "Render Deploy")
)

   app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()


if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')

