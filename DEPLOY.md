# EC2 Deployment

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "userbot"
git branch -M main
git remote add origin https://github.com/YOU/session-bot.git
git push -u origin main
```

### 2. On EC2 (Ubuntu)
```bash
# Install Node.js for pm2
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs git python3-venv
sudo npm i -g pm2

# Clone
git clone https://github.com/YOU/session-bot.git
cd session-bot

# Setup env
cp .env.example .env
nano .env  # Add API_ID, API_HASH, SESSION_STRING

# Install
python3 -m venv venv
source venv/bin/activate
pip install -U pip -r requirements.txt

# Start with pm2
pm2 start bot.py --name session-bot --interpreter $(pwd)/venv/bin/python3
pm2 save
pm2 startup  # follow the command it shows
```

### Commands
```bash
pm2 logs session-bot    # view logs
pm2 restart session-bot # restart
pm2 stop session-bot    # stop
```

Update from Telegram: `.update`