import asyncio
from datetime import datetime
from pyrogram import Client, filters, enums
from config import PREFIX

@Client.on_message(filters.command("bcdm", PREFIX) & filters.me)
async def bcdm(client, m):
    """ .bcdm 2 hello - broadcast to all DMs with 2s interval """
    cmd = m.text.split(maxsplit=2)
    if len(cmd) < 3:
        return await m.edit("Usage: .bcdm <interval> <text>")
    
    interval = float(cmd[1])
    text = cmd[2]
    msg = m.reply_to_message
    
    await m.edit("Fetching DMs...")
    users = []
    async for d in client.get_dialogs():
        if d.chat.type == enums.ChatType.PRIVATE and not d.chat.is_bot:
            users.append(d.chat.id)
    
    await m.edit(f"Broadcasting to {len(users)}...")
    for uid in users:
        try:
            if msg: await msg.copy(uid)
            else: await client.send_message(uid, text)
            await asyncio.sleep(interval)
        except: pass
    await m.edit("✅ DM broadcast done")

@Client.on_message(filters.command("sbcdm", PREFIX) & filters.me)
async def sbcdm(client, m):
    """ .sbcdm 2025-12-25_10:00 2 hello """
    cmd = m.text.split(maxsplit=3)
    if len(cmd) < 4:
        return await m.edit("Usage: .sbcdm YYYY-MM-DD_HH:MM interval text")
    
    run_at = datetime.strptime(cmd[1], "%Y-%m-%d_%H:%M")
    interval = float(cmd[2])
    text = cmd[3]
    
    async def job():
        users = []
        async for d in client.get_dialogs():
            if d.chat.type == enums.ChatType.PRIVATE and not d.chat.is_bot:
                users.append(d.chat.id)
        for uid in users:
            try:
                await client.send_message(uid, text)
                await asyncio.sleep(interval)
            except: pass
    
    client.scheduler.add_job(job, 'date', run_date=run_at)
    await m.edit(f"⏰ Scheduled for {run_at}")

@Client.on_message(filters.command("bcc", PREFIX) & filters.me)
async def bcc(client, m):
    """ .bcc hello - broadcast to contacts """
    text = m.text.split(maxsplit=1)[1] if len(m.command) > 1 else None
    if not text and not m.reply_to_message:
        return await m.edit("Usage: .bcc <text>")
    
    await m.edit("Fetching contacts...")
    contacts = await client.get_contacts()
    for u in contacts:
        try:
            if m.reply_to_message: await m.reply_to_message.copy(u.id)
            else: await client.send_message(u.id, text)
            await asyncio.sleep(2)
        except: pass
    await m.edit(f"✅ Sent to {len(contacts)} contacts")