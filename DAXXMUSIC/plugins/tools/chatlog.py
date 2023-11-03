import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/c56fbe380ab8a1e1331f7.jpg",
    "https://telegra.ph/file/33e81ea80303222535029.jpg",
    "https://telegra.ph/file/47d4c3a58f6b807fdea4a.jpg",
    "https://telegra.ph/file/1466d484f1ecd8cdaa750.jpg",
    "https://telegra.ph/file/2073ab1c1e956f57b54d5.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"☼︎ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #NEW_GROUP ☼︎\n\n"
                f"⚊⚊⚊⚊⚊⚊✬✥✬⚊⚊⚊⚊⚊⚊⚊⚊✬✥✬⚊⚊⚊⚊⚊⚊\n\n"
                f"☼︎ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ⋆ ➺ {message.chat.title}\n"
                f"☼︎ ɢʀᴏᴜᴘ ɪᴅ ⋆ ➺ {message.chat.id}\n"
                f"☼︎ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ⋆ ➺ @{message.chat.username}\n"
                f"☼︎ ɢʀᴏᴜᴘ ʟɪɴᴋ ⋆ ➺[ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"☼︎ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ⋆ ➺ {count}\n"
                f"☼︎ ᴀᴅᴅᴇᴅ ʙʏ ⋆ ➺ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"☼︎ sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ ☼︎", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "☼︎ ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ ☼︎"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "☼︎ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ☼︎"
        chat_id = message.chat.id
        left = f"✵ <b><u>#LEFT_GROUP</u></b> ✵\n\n☼︎ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ⋆ ➺ {title}\n\n☼︎ ɢʀᴏᴜᴘ ɪᴅ ⋆ ➺ {chat_id}\n\n☼︎ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ⋆ ➺ {remove_by}\n\n☼︎ ʙᴏᴛ ɴᴀᴍᴇ ⋆ ➺ @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷 @{member.username} ☼︎ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɴᴇᴡ ɢʀᴏᴜᴘ ☼︎\n\n"
                f"☼︎ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ⋆ ➺ {message.chat.title}\n"
                f"☼︎ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ⋆ ➺ @{message.chat.username}\n"
                f"☼︎ ʏᴏᴜʀ ɪᴅ ⋆ ➺ {member.id}\n"
                f"☼︎ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ⋆ ➺ @{member.username}\n"
                f"☼︎ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴏᴛᴇʟ {count} ᴍᴇᴍʙᴇʀs ☼︎"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"☼︎ ᴀᴅᴅ ᴛᴏ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☼︎", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#tagall
