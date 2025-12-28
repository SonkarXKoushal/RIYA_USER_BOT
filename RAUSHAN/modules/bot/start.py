from RAUSHAN import app
from config import ALIVE_PIC
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OWNER_ID = 8142003954

MAIN_TEXT = (
    "✦𝗛𝗘𝗬..! 𝗧𝗛𝗜𝗦..!!👋 𝗥𝗜𝗬𝗔 𝗨𝗦𝗘𝗥 𝗕𝗢𝗧\n\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗦𝗣𝗔𝗠 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦\n"
    "➪ 𝗕𝗘𝗦𝗧 𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘\n"
    "➪ 𝗠𝗔𝗞𝗘 𝗬𝗢𝗨𝗥 𝗜𝗗-𝗨𝗦𝗘𝗥𝗕𝗢𝗧 /clone\n\n"
    "๏ 𝗨𝗣𝗧𝗜𝗠𝗘 » ONLINE ✅"
)

# ================= START =================
@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = []

    # ROW 1 → HELP + OWNER (owner ko hi dikhega)
    if msg.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("🆘 HELP", callback_data="help"),
            InlineKeyboardButton("👑 OWNER", callback_data="owner")
        ])
    else:
        buttons.append([
            InlineKeyboardButton("🆘 HELP", callback_data="help")
        ])

    # ROW 2 → SUPPORT
    buttons.append([
        InlineKeyboardButton("⚡ SUPPORT", url="https://t.me/riya_chat_support")
    ])

    # ROW 3 → UPDATES
    buttons.append([
        InlineKeyboardButton("⚡ UPDATES", url="https://t.me/riyaupdates")
    ])

    await msg.reply_photo(
        photo=ALIVE_PIC,
        caption=MAIN_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ================= HELP =================
@app.on_callback_query(filters.regex("^help$"))
async def help_menu(_, cb):
    await cb.message.edit_caption(
        caption=(
            "🆘 **HELP MENU**\n\n"
            "• /start – bot start kare\n"
            "• /clone – userbot clone kare\n\n"
            "Baaki features baad me add honge."
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ BACK", callback_data="back")]
        ])
    )

# ================= OWNER =================
@app.on_callback_query(filters.regex("^owner$"))
async def owner_panel(_, cb):
    if cb.from_user.id != OWNER_ID:
        return await cb.answer("❌ Access Denied", show_alert=True)

    await cb.message.edit_caption(
        caption=(
            "👑 **OWNER PANEL**\n\n"
            "• /broadcast\n"
            "• /stats\n"
            "• /ban\n"
            "• /unban\n\n"
            "Owner-only controls."
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ BACK", callback_data="back")]
        ])
    )

# ================= BACK =================
@app.on_callback_query(filters.regex("^back$"))
async def back_menu(_, cb):
    buttons = []

    if cb.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("🆘 HELP", callback_data="help"),
            InlineKeyboardButton("👑 OWNER", callback_data="owner")
        ])
    else:
        buttons.append([
            InlineKeyboardButton("🆘 HELP", callback_data="help")
        ])

    buttons.append([
        InlineKeyboardButton("⚡ SUPPORT", url="https://t.me/riya_chat_support")
    ])
    buttons.append([
        InlineKeyboardButton("⚡ UPDATES", url="https://t.me/riyaupdates")
    ])

    await cb.message.edit_caption(
        caption=MAIN_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
