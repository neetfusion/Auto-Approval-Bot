from os import getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    
    # Your Force Subscribe Channel Id
    CHID = int(getenv("CHID", ""))  # Make the bot admin in this channel
    
    # Bot owners (use space-separated user IDs in env)
    SUDO = list(map(int, getenv("SUDO", "").split()))
    
    # MongoDB connection URI
    MONGO_URI = getenv("MONGO_URI", "")

cfg = Config()
