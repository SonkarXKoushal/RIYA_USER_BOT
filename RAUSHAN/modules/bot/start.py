from RAUSHAN import app
from config import ALIVE_PIC
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔴 APNI NUMERIC TELEGRAM ID
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

    if msg.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("👑 OWNER PANEL", callback_data="owner")
        ])

    buttons.extend([
        [InlineKeyboardButton("🆘 HELP", callback_data="help")],
        [InlineKeyboardButton("⚡ CHANNEL 💕", url="https://t.me/ajisbackk")],
        [InlineKeyboardButton("⚡ SUPPORT 💕", url="https://t.me/TEAM_RIYA_SUPPORT")]
    ])

    await msg.reply_photo(
        photo=ALIVE_PIC,
        caption=MAIN_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ================= OWNER PANEL =================
@app.on_callback_query(filters.regex("^owner$"))
async def owner_panel(_, cb):
    if cb.from_user.id != OWNER_ID:
        return await cb.answer("❌ Access Denied", show_alert=True)

    await cb.message.edit_caption(
        caption=(
            "👑 **OWNER PANEL**\n\n"
            "Available controls:\n"
            "• /broadcast – message sabko bhejo\n"
            "• /stats – bot stats\n"
            "• /ban – user block\n"
            "• /unban – unblock user\n\n"
            "⚠️ Commands baad me implement kiye ja sakte hain."
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="back")]
        ])
    )

# ================= HELP =================
@app.on_callback_query(filters.regex("^help$"))
async def help_menu(_, cb):
    await cb.message.edit_caption(
        caption=(
            "🆘 **HELP MENU**\n\n"
            "Available Commands:\n\n"
            "• /start → bot start kare\n"
            "• /clone → userbot clone kare\n\n"
            "📌 Baaki commands future update me add honge."
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="back")]
        ])
    )

# ================= BACK =================
@app.on_callback_query(filters.regex("^back$"))
async def back_menu(_, cb):
    buttons = []

    if cb.from_user.id == OWNER_ID:
        buttons.append([
            InlineKeyboardButton("👑 OWNER PANEL", callback_data="owner")
        ])

    buttons.extend([
        [InlineKeyboardButton("🆘 HELP", callback_data="help")],
        [InlineKeyboardButton("⚡ CHANNEL 💕", url="https://t.me/ajisbackk")],
        [InlineKeyboardButton("⚡ SUPPORT 💕", url="https://t.me/TEAM_RIYA_SUPPORT")]
    ])

    await cb.message.edit_caption(
        caption=MAIN_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
