from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# 🔴 CHANGE THIS TO YOUR TELEGRAM NUMERIC ID
OWNER_ID = 8142003954 

PHONE_NUMBER_TEXT = (
    " ✦𝗛𝗘𝗬..! 𝗧𝗛𝗜𝗦..!!👋! 𝗥𝗜𝗬𝗔 𝗨𝗦𝗘𝗥 𝗕𝗢𝗧\n\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗦𝗣𝗔𝗠 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘\n"
    "➪ 𝗠𝗔𝗞𝗘 𝗬𝗢𝗨𝗥 𝗜𝗗-𝗨𝗦𝗘𝗥𝗕𝗢𝗧 /clone\n\n"
    "๏ 𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥 : 270\n"
    "๏ 𝗧𝗢𝗧𝗔𝗟 𝗔𝗖𝗧𝗜𝗩𝗘 𝗨𝗦𝗘𝗥 : 215\n"
    "๏ 𝗨𝗣𝗧𝗜𝗠𝗘 » 1h:23m:19s"
)

# ================= START =================
@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    buttons = []

    # OWNER BUTTON (sirf owner ko)
    if message.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("👑 OWNER PANEL", callback_data="owner_panel")
        ])

    # HELP BUTTON
    buttons.append([
        InlineKeyboardButton("🆘 HELP", callback_data="help_menu")
    ])

    # NORMAL LINKS
    buttons.append([
        InlineKeyboardButton("⚡ CHANNEL 💕", url="https://t.me/ajisbackk")
    ])
    buttons.append([
        InlineKeyboardButton("⚡ SUPPORT 💕", url="https://t.me/TEAM_RIYA_SUPPORT")
    ])

    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_PIC,
        caption=PHONE_NUMBER_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# ================= OWNER PANEL =================
@app.on_callback_query(filters.regex("^owner_panel$"))
async def owner_panel(client, callback):
    if callback.from_user.id != OWNER_ID:
        return await callback.answer("❌ Access Denied", show_alert=True)

    await callback.message.edit_text(
        "👑 **OWNER PANEL**\n\n"
        "Yahan baad me commands add kar sakte ho:\n\n"
        "• /broadcast\n"
        "• /stats\n"
        "• /ban\n"
        "• /unban\n"
    )


# ================= HELP MENU =================
@app.on_callback_query(filters.regex("^help_menu$"))
async def help_menu(client, callback):
    await callback.message.edit_text(
        "🆘 **HELP MENU**\n\n"
        "/start – bot start kare\n"
        "/clone – userbot clone kare\n\n"
        "Baaki commands aap baad me add kar sakte ho."
    )


# ================= CLONE COMMAND =================
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    if len(msg.command) < 2:
        return await msg.reply("❌ Usage:\n\n`/clone session_string`")

    phone = msg.command[1]
    text = await msg.reply("⏳ Please wait...")

    try:
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=phone,
            plugins=dict(root="RAUSHAN/modules")
        )
        await client.start()
        user = await client.get_me()

        await text.edit(
            f"✅ **Clone Successful!**\n\n"
            f"User: `{user.first_name}`"
        )

    except Exception as e:
        await text.edit(f"❌ ERROR:\n`{str(e)}`")
