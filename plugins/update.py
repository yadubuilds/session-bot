import os
from pyrogram import Client, filters
from config import PREFIX

@Client.on_message(filters.command("update", PREFIX) & filters.me)
async def update(_, m):
    await m.edit("🔄 Updating...")
    os.system("git pull")
    await m.edit("✅ Updated! Restarting...")
    os.system("pm2 restart session-bot")

@Client.on_message(filters.command("restart", PREFIX) & filters.me)
async def restart(_, m):
    await m.edit("♻️ Restarting...")
    os.system("pm2 restart session-bot")