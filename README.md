# Session Bot - Pyrogram Userbot

Simple userbot with all broadcast plugins. Uses SESSION_STRING (no login needed).

## Features
- `.update` / `.restart` - git pull & pm2 restart
- `.bcdm 2 hello` - broadcast to all DMs (2s interval)
- `.sbcdm 2025-12-25_10:00 2 hello` - schedule DM broadcast
- `.bcc hello` - broadcast to contacts
- `.story` (reply to media) - post story
- `.add +91... Name` - save contact
- `.req @group msg` - DM all join requests with group link
- `.bcg @group 2 hello` - broadcast to group members
- `.sbcg @group 2025-12-25_10:00 2 hello` - schedule group broadcast

## Setup Local
```bash
pip install -r requirements.txt
# fill .env then
python bot.py
```

## Deploy to EC2
```bash
git clone https://github.com/YOU/session-bot.git
cd session-bot
cp .env.example .env
# edit .env with your API_ID, API_HASH, SESSION_STRING
python3 -m venv venv
source venv/bin/activate
pip install -U pip -r requirements.txt
pm2 start bot.py --name session-bot --interpreter $(pwd)/venv/bin/python3
pm2 save
pm2 startup
```