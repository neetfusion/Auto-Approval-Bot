from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "27846034"))
    API_HASH = getenv("API_HASH", "980caee71c20f6babaf86d985f5af9e5")
    BOT_TOKEN = getenv("BOT_TOKEN", "7976191427:AAFYxlIWAaDPPBeYBwgh3GKT1ysfUP_ceGI")
    
    # Your Force Subscribe Channel Id
    CHID = int(getenv("CHID", "-1002220587356"))  # Make the bot admin in this channel
    
    # Bot owners (use space-separated user IDs in env)
    SUDO = list(map(int, getenv("SUDO", "1320989352").split()))
    
    # MongoDB connection URI
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://neetfusionin:neetfusionin@cluster0.c7aecmc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()
