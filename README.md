# Auto-Approval-Bot

This is an Auto Approval Bot for Telegram groups and channels, developed by **Hunter**. The bot automatically approves pending join requests in groups and channels and provides several commands for admins to manage users and send broadcasts.

## Features

- **Auto Approve Requests:** The bot automatically approves requests in groups and channels where it has admin rights.
- **Pending Request Approval:** Admins can approve all pending requests at once with a simple confirmation.
- **Custom Start Message:** Upon starting the bot, users will receive a personalized welcome message.
- **Channel Join Requirement:** The bot checks if a user has joined the bot's required channel before approving them.
- **Broadcast Commands:** The bot can send broadcast messages to all users in the database.
- **User Stats:** Admins can query the total number of users and groups where the bot is active.
  
## Commands

### 1. `/start`
- Sends a welcome message to users with a photo and description of the bot's capabilities.

### 2. `/users`
- Sends stats about the number of users and groups the bot is serving. Only available to sudo admins.

### 3. `/bcast`
- Allows the bot owner to send a broadcast message to all users. Only available to sudo admins.
  
### 4. `/fcast`
- Similar to `/bcast`, but it forwards a message to all users. Only available to sudo admins.

### 5. `/approve_all_pending`
- Approves all pending join requests in the group or channel. Admins will be asked for confirmation before proceeding.

## How to Deploy
Koyeb And Render 

### 1. Clone the repository
```bash
git clone https://github.com/Anime019ongoing/Auto-Approval-Bot.git

pip install -r requirements.txt

Needed Variables
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_telegram_bot_token
CHID=your_channel_id_for_forced_subscription
SUDO=your_telegram_user_id
MONGO_URI=your_mongodb_connection_uri
Run Bot
python bot.py

Credits

Bot Developer: Hunter

Project Repository: GitHub - Anime019ongoing
