from pymongo import MongoClient
from configs import cfg

client = MongoClient(cfg.MONGO_URI)

users = client['main']['users']
groups = client['main']['groups']

# Check if the user exists in the database
def already_db(user_id):
    user = users.find_one({"user_id": str(user_id)})
    return user is not None

# Check if the group exists in the database
def already_dbg(chat_id):
    group = groups.find_one({"chat_id": str(chat_id)})
    return group is not None

# Add a user to the database if they don't exist
def add_user(user_id):
    if already_db(user_id):
        return False  # User already exists
    try:
        users.insert_one({"user_id": str(user_id)})
        return True  # Successfully added user
    except Exception as e:
        print(f"Error adding user {user_id}: {e}")
        return False

# Remove a user from the database if they exist
def remove_user(user_id):
    if not already_db(user_id):
        return False  # User doesn't exist
    try:
        users.delete_one({"user_id": str(user_id)})
        return True  # Successfully removed user
    except Exception as e:
        print(f"Error removing user {user_id}: {e}")
        return False

# Add a group to the database if it doesn't exist
def add_group(chat_id):
    if already_dbg(chat_id):
        return False  # Group already exists
    try:
        groups.insert_one({"chat_id": str(chat_id)})
        return True  # Successfully added group
    except Exception as e:
        print(f"Error adding group {chat_id}: {e}")
        return False

# Count the number of users in the database
def all_users():
    try:
        return len(list(users.find({})))
    except Exception as e:
        print(f"Error counting users: {e}")
        return 0

# Count the number of groups in the database
def all_groups():
    try:
        return len(list(groups.find({})))
    except Exception as e:
        print(f"Error counting groups: {e}")
        return 0
