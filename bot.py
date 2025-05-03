from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

# Function to check if the user is an admin
async def is_admin(chat_id, user_id):
    try:
        chat_member = await app.get_chat_member(chat_id, user_id)
        return chat_member.status in ['administrator', 'creator']
    except Exception:
        return False

# Main process when a new join request is received
@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        await app.send_message(kk.id, "**Hello {}!\nWelcome To {}\n\n__Powerd By : Anime Flasher__**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("User isn't started bot (means group)")
    except Exception as err:
        print(str(err))

# Admin notification for pending requests
@app.on_message(filters.command("approve_all") & filters.user(cfg.SUDO))
async def approve_all_request(_, m: Message):
    chat_id = m.chat.id
    pending_requests = await app.get_chat_join_requests(chat_id)
    if not pending_requests:
        await m.reply("No pending requests!")
        return

    # Ask the admin if they want to approve all pending requests
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ Yes, Approve All", callback_data="approve_all_yes"),
             InlineKeyboardButton("❌ No, Cancel", callback_data="approve_all_no")]
        ]
    )
    await m.reply("Boss, should I approve all pending requests?", reply_markup=keyboard)

# Handle admin's response to approve or cancel all requests
@app.on_callback_query(filters.regex("approve_all_yes"))
async def approve_all_yes(_, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    pending_requests = await app.get_chat_join_requests(chat_id)
    for req in pending_requests:
        try:
            await app.approve_chat_join_request(chat_id, req.user.id)
            await app.send_message(req.user.id, "🍁 Your request has been approved! Welcome to the group!")
            add_user(req.user.id)
        except Exception as e:
            print(f"Error approving request: {e}")
    await cb.edit_message_text("✅ All pending requests have been approved!")

@app.on_callback_query(filters.regex("approve_all_no"))
async def approve_all_no(_, cb: CallbackQuery):
    await cb.edit_message_text("❌ Operation canceled. No pending requests were approved.")

# Start message when a user starts the bot
@app.on_message(filters.private & filters.command("start"))
async def start(_, m: Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id)
    except:
        try:
            invite_link = await app.create_chat_invite_link(int(cfg.CHID))
        except:
            await m.reply("**Make Sure I Am Admin In Your Channel**")
            return
        key = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Join Channel", url=invite_link.invite_link),
                InlineKeyboardButton("Try Again!", callback_data="chk")
            ]]
        )
        await m.reply_text("**⚠️ Access Denied! ⚠️\n\nPlease join my update channel to use me. If you've joined the channel, click on 'Check Again' to confirm.**", reply_markup=key)
        return

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🗯 Channel", url="https://t.me/Anime_Flasher"),
            InlineKeyboardButton("💬 Support", url="https://t.me/weoo_chats")
        ]]
    )

    await m.reply_photo("https://i.ibb.co/CKHPGqWD/f1724820ad0b.jpg", caption="🍁 Hello {}!\nI’m an auto approve bot. I can approve users in groups & channels. Add me to your chat and promote me to admin with 'add members' permission.".format(m.from_user.mention), reply_markup=keyboard)

# Admin broadcast tool (for sending messages to all users)
@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ Successfully sent to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` blocked users.\n👻 Found `{deactivated}` deactivated users.")

print("I'm alive now! Thx To @Otakukart7")
app.run()
