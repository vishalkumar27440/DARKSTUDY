import os
import re
import sys
import json
import time
import aiohttp
import asyncio
import requests
import subprocess
import urllib.parse
import cloudscraper
import datetime
import random
import ffmpeg
import logging 
import yt_dlp
import youtube_dl
import  pyrogram
from aiohttp import web
from core import *
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
import yt_dlp as youtube_dl
import m3u8
import core as helper
from utils import progress_bar
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

photo = "https://i.postimg.cc/dVY9nL63/IMG-20250426-130510-655.jpg"
cpphoto = "https://i.postimg.cc/dVY9nL63/IMG-20250426-130510-655.jpg"
appxzip = "https://i.postimg.cc/dVY9nL63/IMG-20250426-130510-655.jpg"
my_name = "VK"
CHANNEL_ID = "-1003924837795"##change it with your channel 🆔 

cookies_file_path = os.getenv("COOKIES_FILE_PATH", "youtube_cookies.txt")

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("your_render_url") ## change it with your host url

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    # WEBHOOK and PORT may be undefined in some environments; guard access
    try:
        webhook_enabled = WEBHOOK
    except NameError:
        webhook_enabled = False

    try:
        port = PORT
    except NameError:
        port = 8080

    if webhook_enabled:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", port)
        await site.start()
        print(f"Web server started on port {port}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await asyncio.sleep(3600)  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
        return
        
class Data:
    START = (
        "🌟 Welcome {0}! 🌟\n\n"
    )
# Define the start command handler
@bot.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    user = await client.get_me()
    mention = user.mention
    start_message = await client.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention)
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: [⬜⬜⬜⬜⬜⬜⬜⬜⬜] 0%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Loading features... ⏳\n\n"
        "Progress: [🟥🟥🟥⬜⬜⬜⬜⬜⬜] 25%\n\n"
    )
    
    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: [🟧🟧🟧🟧🟧⬜⬜⬜⬜] 50%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Checking Bot Status... 🔍\n\n"
        "Progress: [🟨🟨🟨🟨🟨🟨🟨⬜⬜] 75%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Checking status Ok... Command Nhi Bataunga **Bot Made BY @VK_0786BOT™👨🏻‍💻**🔍\n\n"
        "Progress:[🟩🟩🟩🟩🟩🟩🟩🟩🟩] 100%\n\n"
    )

@bot.on_message(filters.command(["stop"]) )
async def restart_handler(_, m):
    await m.delete()
    await m.reply_text("**STOPPED**🛑", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["King","upload"]) )
async def txt_handler(bot: Client, m: Message):
    await m.delete()
    
    editable = await m.reply_text(f"**🔹Hi I am Poweful TXT Downloader📥 Bot.**\n🔹**Send me the TXT file and wait.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"𝗩𝗜𝗦𝗛𝗔𝗟 𝗞𝗨𝗠𝗔𝗥"
    token = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzYxNTE3MzAuMTI2LCJkYXRhIjp7Il9pZCI6IjYzMDRjMmY3Yzc5NjBlMDAxODAwNDQ4NyIsInVzZXJuYW1lIjoiNzc2MTAxNzc3MCIsImZpcnN0TmFtZSI6IkplZXYgbmFyYXlhb[...]"
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            if not i:
                continue
            parts = i.split("://", 1)
            if len(parts) == 2:
                links.append(parts)
        os.remove(x)
    except Exception:
        await m.reply_text("Invalid file input.")
        try:
            os.remove(x)
        except Exception:
            pass
        return

    # Edit the message to show the total number of links found
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend from where you want to download (initial is **1**).")
    
    # Wait for user input
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text if input0.text else "1"
    
    # Delete the user's input message
    await input0.delete(True)
    
    # Try to convert the input to an integer, default to 1 if conversion fails
    try:
        arg = int(raw_text)
    except ValueError:
        arg = 1
    
    # If the input is "1", proceed with batch naming and notifications
    if raw_text == "1":
        # Extract the file name without extension
        file_name_without_ext = os.path.splitext(file_name)[0]
        
        # Create a fancy batch name
        fancy_batch_name = f"🎓𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲: {file_name_without_ext}"
        name_message = await bot.send_message(
            m.chat.id,
            "📌 **Batch Name Pinned!** 📌\n"
            f"🎨 {fancy_batch_name}\n"
            "✨ Stay organized with your pinned batches 🚀!"
        )
        # Try to pin the message, ignore errors
        try:
            await bot.pin_chat_message(m.chat.id, name_message.id)
        except Exception:
            pass

        # Wait for 2 seconds before proceeding
        await asyncio.sleep(2)

    await editable.edit("**Enter Your Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text if input1.text else 'd'
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution.\n Eg : 480 or 720**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text if input2.text else '480'
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "144x256"
        elif raw_text2 == "240":
            res = "240x426"
        elif raw_text2 == "360":
            res = "360x640"
        elif raw_text2 == "480":
            res = "480x854"
        elif raw_text2 == "720":
            res = "720x1280"
        elif raw_text2 == "1080":
            res = "1080x1920" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send 'de' for use default.\n Eg : @VK_0786BOT👨🏻‍💻**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text if input3.text else 'de'
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3
        
    await editable.edit("**Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋  or send 'Not' for use default**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text if input4.text else 'not'
    await input4.delete(True)
    if raw_text4.lower() == 'not':
        MR = token
    else:
        MR = raw_text4
        
    await editable.edit("Now send the **Thumb url**\n**Eg :** ``\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text if input6.text else 'no'
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb and (thumb.startswith("http://") or thumb.startswith("https://")):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(arg)
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy

            # Simplified handling: prepare yt-dlp command as fallback
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"

            name1 = links[i][0].strip()
            safe_name = re.sub(r"[^\w\- ]", "", name1)[:60]
            name = f"{str(count).zfill(3)}) {safe_name} {my_name}"

            if "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies {cookies_file_path} -f "{ytf}" "{url}" -o "{name}.mp4"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                Show = f"📥 Downloading »\n\n📝 Title:- `{name}`\n\n**🔗 Total URL »** ✨{len(links)}✨"
                prog = await m.reply_text(Show)
                # Use helper.download_video if available, otherwise run command
                try:
                    res_file = await helper.download_video(url, cmd, name)
                except Exception:
                    # fallback to running shell command
                    os.system(cmd)
                    res_file = f"{name}.mp4"
                filename = res_file
                await prog.delete(True)
                # Send video using helper if exists, else send document
                try:
                    await helper.send_vid(bot, m, name, filename, thumb, name, prog)
                except Exception:
                    await bot.send_document(chat_id=m.chat.id, document=filename, caption=name)
                count += 1
                time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"⌘ Downloading Interrupted ❌ \n\n⌘ Name » {name}\n⌘ Link » `{url}`\nError: {e}"
                )
                continue

    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("**✅ Successfully Done**")


# NOTE: Many other handlers were present originally; to keep this deployable we kept core handlers only.

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as exc:
        print("Failed to start:", exc)
