from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# 🔴 APNI NUMERIC TELEGRAM ID YAHA DALO
OWNER_ID = 123456789  

PHONE_NUMBER_TEXT = (
    " ✦𝗛𝗘𝗬..! 𝗧𝗛𝗜𝗦..!!👋! 𝗥𝗜𝗬𝗔 𝗨𝗦𝗘𝗥 𝗕𝗢𝗧\n\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗦𝗣𝗔𝗠 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘\n"
    "➪ 𝗠𝗔𝗞𝗘 𝗬𝗢𝗨𝗥 𝗜𝗗-𝗨𝗦𝗘𝗥𝗕𝗢𝗧 /clone\n\n"
    "๏ 𝗨𝗣𝗧𝗜𝗠𝗘 » Online ✅"
)

# ================= START =================
@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    buttons = []

    if message.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("👑 OWNER PANEL", callback_data="owner_panel")
        ])

    buttons.append([
        InlineKeyboardButton("🆘 HELP", callback_data="help_menu")
    ])

    buttons.append([
        InlineKeyboardButton("⚡ CHANNEL", url="https://t.me/ajisbackk")
    ])
    buttons.append([
        InlineKeyboardButton("⚡ SUPPORT", url="https://t.me/TEAM_RIYA_SUPPORT")
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

    await callback.message.edit_caption(
        caption=
        "👑 **OWNER PANEL**\n\n"
        "Yahan baad me commands add kar sakte ho:\n\n"
        "• /broadcast\n"
        "• /stats\n"
        "• /ban\n"
        "• /unban",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="back_home")]
        ])
    )

# ================= HELP MENU =================
@app.on_callback_query(filters.regex("^help_menu$"))
async def help_menu(client, callback):
    await callback.message.edit_caption(
        caption=
        "🆘 **HELP MENU**\n\n"
        "/start – bot start kare\n"
        "/clone – userbot clone kare\n\n"
        "Baaki commands baad me add honge.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="back_home")]
        ])
    )

# ================= BACK BUTTON =================
@app.on_callback_query(filters.regex("^back_home$"))
async def back_home(client, callback):
    buttons = []

    if callback.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("👑 OWNER PANEL", callback_data="owner_panel")
        ])

    buttons.append([
        InlineKeyboardButton("🆘 HELP", callback_data="help_menu")
    ])
    buttons.append([
        InlineKeyboardButton("⚡ CHANNEL", url="https://t.me/ajisbackk")
    ])
    buttons.append([
        InlineKeyboardButton("⚡ SUPPORT", url="https://t.me/TEAM_RIYA_SUPPORT")
    ])

    await callback.message.edit_caption(
        caption=PHONE_NUMBER_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ================= CLONE =================
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    if len(msg.command) < 2:
        return await msg.reply("❌ Usage:\n`/clone session_string`")

    session = msg.command[1]
    wait = await msg.reply("⏳ Please wait...")

    try:
        client = Client(
            name="CloneSession",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="RAUSHAN/modules")
        )
        await client.start()
        user = await client.get_me()

        await wait.edit(
            f"✅ **Clone Successful!**\n\n"
            f"👤 User: `{user.first_name}`"
        )

    except Exception as e:
        await wait.edit(f"❌ ERROR:\n`{e}`")
