from pyrogram import Client, filters, types
from config import PREFIX

@Client.on_message(filters.command("add", PREFIX) & filters.me)
async def add(client, m):
    """ .add +919876543210 John """
    cmd = m.text.split(maxsplit=2)
    if len(cmd) < 3:
        return await m.edit("Usage: .add phone firstname")
    
    phone, name = cmd[1], cmd[2]
    await client.import_contacts([types.InputPhoneContact(phone, name)])
    await m.edit(f"✅ Saved {name}")