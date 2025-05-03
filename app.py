from pyrogram import Client
from configs import cfg

app = Client(
    "approver",               # Session name
    api_id=cfg.API_ID,        # API ID from Telegram Developer
    api_hash=cfg.API_HASH,    # API hash from Telegram Developer
    bot_token=cfg.BOT_TOKEN   # Bot token from BotFather
)

# Start the bot
def start_bot():
    app.run()

if __name__ == "__main__":
    print("Bot is starting...")
    start_bot()
