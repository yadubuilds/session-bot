from pyrogram import Client, filters
from config import PREFIX

@Client.on_message(filters.command("story", PREFIX) & filters.me)
async def story(client, m):
    """ .story caption - reply to photo/video """
    if not m.reply_to_message:
        return await m.edit("Reply to photo/video")
    
    caption = m.text.split(maxsplit=1)[1] if len(m.command) > 1 else ""
    await m.edit("Posting story...")
    
    file = await client.download_media(m.reply_to_message)
    await client.send_story("me", file, caption=caption)
    await m.edit("✅ Story posted")