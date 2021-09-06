from time import time
from datetime import datetime
from helpers.filters import command
from helpers.decorators import sudo_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery
from config import BOT_USERNAME


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, m: Message):
   if m.chat.type == "private":
      await m.reply(f"✨ **Hallo anak haram ngapain lu kesini ngentod.**\n\n💭 **Saya dibuat untuk nonton film movie bukan bokep ya mek.**\n\n❔ **oke intinya fandi ganteng, hayolo saya entod kamu hehe** 🖕",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ CARA MENGGUNAKAN BOT KEREN INI", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 FANDI GANTENG YA MEK", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "💬 ASET NEGARA", url="https://t.me/asetnegaragaktuh"),
                          InlineKeyboardButton(
                             "📣 STORY FANDI", url="https://t.me/storyfandi")
                       ],[
                          InlineKeyboardButton(
                             "☣️ OWNER GANTENG", url="https://t.me/dlwrml")
                       ],[
                          InlineKeyboardButton(
                             "📚 PENGGUNAAN BOT KEREN", callback_data="cblist")
                       ]]
                    ))
   else:
      await m.reply("**✨ BOT KEREN NYA IDUP WOW  ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ CARA MENGGUNAKAN BOT KEREN", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 CARI DI YOUTUBE", switch_inline_query='')
                       ],[
                          InlineKeyboardButton(
                             "📚 CMD BOT NYA MEK", callback_data="cblist")
                       ]]
                    )
      )


@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **BOT NYA BISA YEAY**\n<b>💠 **HIDUP MEK:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ ASET NEGARA", url=f"https://t.me/asetnegaragaktuh"
                    ),
                    InlineKeyboardButton(
                        "📣 STORY FANDI", url=f"https://t.me/storyfandi"
                    ),
                    InlineKeyboardButton(
                        "☣️ OWNER KECE", url=f"https://t.me/kemeemm"
                    )
                ]

            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    start = time()
    m_reply = await m.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🐊 `peler!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"fandi ganteng ya njing@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 Bot keren:\n"
        f"• **mekii:** `{uptime}`\n"
        f"• **udah mulai ya mek:** `{START_TIME_ISO}`"
    )
