from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import API_ID, API_HASH, SESSION_STRING

app = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins=dict(root="plugins")
)

scheduler = AsyncIOScheduler()
app.scheduler = scheduler

if __name__ == "__main__":
    scheduler.start()
    print("Userbot started...")
    app.run()