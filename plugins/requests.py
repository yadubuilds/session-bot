import asyncio
from pyrogram import Client, filters
from config import PREFIX

@Client.on_message(filters.command("req", PREFIX) & filters.me)
async def req(client, m):
    """ .req @group hello """
    cmd = m.text.split(maxsplit=2)
    if len(cmd) < 3:
        return await m.edit("Usage: .req <chat> <message>")
    
    chat, text = cmd[1], cmd[2]
    await m.edit("Fetching requests...")
    
    link = (await client.get_chat(chat)).invite_link or await client.export_chat_invite_link(chat)
    
    count = 0
    async for r in client.get_chat_join_requests(chat):
        try:
            await client.send_message(r.user.id, f"{text}\n\n{link}")
            count += 1
            await asyncio.sleep(2)
        except: pass
    await m.edit(f"✅ Messaged {count} requests")