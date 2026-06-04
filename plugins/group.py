import asyncio
from datetime import datetime
from pyrogram import Client, filters
from config import PREFIX

@Client.on_message(filters.command("bcg", PREFIX) & filters.me)
async def bcg(client, m):
    """ .bcg @group 2 hello """
    cmd = m.text.split(maxsplit=3)
    if len(cmd) < 4:
        return await m.edit("Usage: .bcg <chat> <interval> <text>")
    
    chat, interval, text = cmd[1], float(cmd[2]), cmd[3]
    await m.edit("Fetching members...")
    
    members = []
    async for mem in client.get_chat_members(chat):
        if not mem.user.is_bot and not mem.user.is_deleted:
            members.append(mem.user.id)
    
    await m.edit(f"Broadcasting to {len(members)}...")
    for uid in members:
        try:
            await client.send_message(uid, text)
            await asyncio.sleep(interval)
        except: pass
    await m.edit("✅ Group broadcast done")

@Client.on_message(filters.command("sbcg", PREFIX) & filters.me)
async def sbcg(client, m):
    """ .sbcg @group 2025-12-25_10:00 2 hello """
    cmd = m.text.split(maxsplit=4)
    if len(cmd) < 5:
        return await m.edit("Usage: .sbcg chat date interval text")
    
    chat = cmd[1]
    run_at = datetime.strptime(cmd[2], "%Y-%m-%d_%H:%M")
    interval = float(cmd[3])
    text = cmd[4]
    
    async def job():
        async for mem in client.get_chat_members(chat):
            try:
                await client.send_message(mem.user.id, text)
                await asyncio.sleep(interval)
            except: pass
    
    client.scheduler.add_job(job, 'date', run_date=run_at)
    await m.edit(f"⏰ Scheduled for {run_at}")