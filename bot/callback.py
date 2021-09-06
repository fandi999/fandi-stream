from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ HOW TO USE THIS BOT:

1.) Masukin bot keren ini ke gc hina lo!.
2.) Jadiin admin bot keren ini ya mek.
3.) Masukin @{bn} ke gc lo yg hina.
4.) Hidupin vcg biar bot nya bisa war ya mek.
5.) Ketik /vstream (reply to video) kontol lo.
6.) Ketik /vstop buat sudahi war di vcg.

📝 **Warning:fandi ganteng ya mek !**

⚡ __bot fandi keren ya mek__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello meki , saya bot movie fandi .**\n\n💭 **gua di buat untuk nonton film tapi bukan bokep ya mek.**\n\n❔ **To find out how to use me, fandi ganteng bgt ya**🖕",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ FANDI GANTENG ", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 PADA INTINYA FANDI FANTENG", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "💬 ASET NEGARA", url="https://t.me/asetnegaragaktuh"),
                          InlineKeyboardButton(
                             "📣 STORY FANDI", url="https://t.me/storyfandi")
                       ],[
                          InlineKeyboardButton(
                             "☣️ OWNER KECE", url="https://t.me/kemeemm")
                       ],[
                          InlineKeyboardButton(
                             "📚 SEMUA PERINTAH", callback_data="cblist")
                       ]]
                    ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **BOT INFORMASI !**

🤖 __INI BOT STREAMING FILM YA MEK TAPI KALO MAU STREAMING BOKEP JELAS GABISA NTAR SAYA DOSA NJING.__

💡 __FANDI GANTENG GEES.__

👨🏻‍💻 __TERIMA KASIH BUAT MANTAN ANJING YANG NINGGALIN PAS LAGI SAYANG SAYANGNYA:__

👩🏻‍✈️ » [Levina Shavila](https://github.com/levina-lab)
🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD)
👩🏻‍✈️ » [Achu Biju](https://github.com/Achu2234)
🤵🏻 » [Mr.Zxce3](https://github.com/Zxce3)
🤵🏻 » [Tofik Denianto](https://github.com/tofikdn)
🤵🏻 » [Shohih Abdul](https://github.com/DoellBarr)

__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )

@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""📚 All Command List:

» /vstream (reply to video or file) - to stream video
» /vstop - end the video streaming
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyric (song name) - lyric scrapper

🎊 FUN CMD:

» /asupan - check it by yourself
» /chika - check it by yourself
» /wibu - check it by yourself
» /truth - check it by yourself
» /dare - check it by yourself

🔰 EXTRA CMD:

» /tts (reply to text) - text to speech
» /alive - check bot alive status
» /ping - check bot ping status
» /uptime - check bot uptime status
» /sysinfo - check bot system information

⚡ __Maintained by Veez Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
