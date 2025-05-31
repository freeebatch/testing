# # from config import CHANNEL_ID, SUDO_USERS 
# # from Extractor.core import script
# # from pyrogram.errors import UserNotParticipant
# # from pyrogram.types import *
# # from Extractor.core.mongo.plans_db import premium_users




# # async def chk_user(query, user_id):
# #     user = await premium_users()
# #     if user_id in user or user_id in SUDO_USERS:
# #         await query.answer("Premium User!!")
# #         return 0
# #     else:
# #         await query.answer("Sir, you don't have premium access!!", show_alert=True)
# #         return 1




# # async def gen_link(app,chat_id):
# #    link = await app.export_chat_invite_link(chat_id)
# #    return link

# # async def subscribe(app, message):
# #    update_channel = CHANNEL_ID
# #    url = await gen_link(app, update_channel)
# #    if update_channel:
# #       try:
# #          user = await app.get_chat_member(update_channel, message.from_user.id)
# #          if user.status == "kicked":
# #             await message.reply_text("Sorry Sir, You are Banned. Contact My Support Group @Shivaay20005")
# #             return 1
# #       except UserNotParticipant:
# #          await message.reply_photo(photo="https://tinypic.host/images/2025/05/01/file_0000000056486230ad1690c7389017ad.png",caption=script.FORCE_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 🤖", url=f"{url}")]]))
# #          return 1
# #       except Exception:
# #          await message.reply_text("Something Went Wrong. Contact My Support Group")
# #          return 1



# # async def get_seconds(time_string):
# #     def extract_value_and_unit(ts):
# #         value = ""
# #         unit = ""

# #         index = 0
# #         while index < len(ts) and ts[index].isdigit():
# #             value += ts[index]
# #             index += 1

# #         unit = ts[index:].lstrip()

# #         if value:
# #             value = int(value)

# #         return value, unit

# #     value, unit = extract_value_and_unit(time_string)

# #     if unit == 's':
# #         return value
# #     elif unit == 'min':
# #         return value * 60
# #     elif unit == 'hour':
# #         return value * 3600
# #     elif unit == 'day':
# #         return value * 86400
# #     elif unit == 'month':
# #         return value * 86400 * 30
# #     elif unit == 'year':
# #         return value * 86400 * 365
# #     else:
# #         return 0







# from config import CHANNEL_ID, SUDO_USERS 
# from Extractor.core import script
# from pyrogram.errors import UserNotParticipant
# from pyrogram.types import *

# # ✅ No longer using: from Extractor.core.mongo.plans_db import premium_users


# # ✅ Cleaned chk_user function
# async def chk_user(query, user_id):
#     if user_id in SUDO_USERS:
#         await query.answer("✅ You are an authorized user!")
#         return 0
#     else:
#         await query.answer("❌ You are not allowed to use this feature!", show_alert=True)
#         return 1


# # ✅ Generates invite link for the updates channel
# async def gen_link(app, chat_id):
#     link = await app.export_chat_invite_link(chat_id)
#     return link


# # ✅ Checks whether user has joined the updates channel
# async def subscribe(app, message):
#     update_channel = CHANNEL_ID
#     url = await gen_link(app, update_channel)

#     if update_channel:
#         try:
#             user = await app.get_chat_member(update_channel, message.from_user.id)
#             if user.status == "kicked":
#                 await message.reply_text("🚫 You are banned! Contact support: @Shivaay20005")
#                 return 1
#         except UserNotParticipant:
#             await message.reply_photo(
#                 photo="https://tinypic.host/images/2025/05/01/file_0000000056486230ad1690c7389017ad.png",
#                 caption=script.FORCE_MSG.format(message.from_user.mention),
#                 reply_markup=InlineKeyboardMarkup([[
#                     InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"{url}")
#                 ]])
#             )
#             return 1
#         except Exception:
#             await message.reply_text("⚠️ Something went wrong! Contact support.")
#             return 1


# # ✅ Time string to seconds converter
# async def get_seconds(time_string):
#     def extract_value_and_unit(ts):
#         value = ""
#         unit = ""

#         index = 0
#         while index < len(ts) and ts[index].isdigit():
#             value += ts[index]
#             index += 1

#         unit = ts[index:].lstrip()

#         return int(value) if value else 0, unit

#     value, unit = extract_value_and_unit(time_string)

#     if unit == 's':
#         return value
#     elif unit == 'min':
#         return value * 60
#     elif unit == 'hour':
#         return value * 3600
#     elif unit == 'day':
#         return value * 86400
#     elif unit == 'month':
#         return value * 86400 * 30
#     elif unit == 'year':
#         return value * 86400 * 365
#     else:
#         return 0








from config import CHANNEL_ID
from Extractor.core import script
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# No authorization or premium checks — open to all users

async def chk_user(query, user_id):
    # Always allow all users (no premium check)
    await query.answer("✅ Access granted: Open to all users!")
    return 0


# Generates invite link for the updates channel
async def gen_link(app, chat_id):
    link = await app.export_chat_invite_link(chat_id)
    return link


# Checks whether user has joined the updates channel (optional)
# You can remove this function altogether if no subscribe check is needed
async def subscribe(app, message):
    update_channel = CHANNEL_ID
    url = await gen_link(app, update_channel)

    if update_channel:
        try:
            user = await app.get_chat_member(update_channel, message.from_user.id)
            if user.status == "kicked":
                await message.reply_text("🚫 You are banned! Contact support: @Shivaay20005")
                return 1
        except UserNotParticipant:
            # Instead of forcing join, just send an info message
            await message.reply_photo(
                photo="https://tinypic.host/images/2025/05/01/file_0000000056486230ad1690c7389017ad.png",
                caption="⚠️ Please join the updates channel to get latest updates.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"{url}")]])
            )
            return 1
        except Exception:
            await message.reply_text("⚠️ Something went wrong! Contact support.")
            return 1
    return 0


# Time string to seconds converter
async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""

        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1

        unit = ts[index:].lstrip()

        return int(value) if value else 0, unit

    value, unit = extract_value_and_unit(time_string)

    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0
