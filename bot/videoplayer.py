import re
from os import path
from asyncio import sleep
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from config import API_ID, API_HASH, SESSION_NAME, BOT_USERNAME
from helpers.decorators import authorized_users_only
from helpers.filters import command


STREAM = {8}
VIDEO_CALL = {}

ydl_opts = {
        "geo-bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)


app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)
group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)


@Client.on_message(command(["vstream", f"vstream@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def vstream(_, m: Message):
    if 1 in STREAM:
        await m.reply_text("😕 **maap gabisa njing**\n\n» **tunggu sampe nenek lo idup lagi!**")
        return

    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await m.reply_text("🔺 **salin link YouTube atau film jangan bokep ya mek!**")

    elif ' ' in m.text:
        msg = await m.reply_text("🔄 **sabar ya kontol...**")
        text = m.text.split(' ', 1)
        query = text[1]
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex,query)
        if match:
            await msg.edit("🔄 **jangan lupa siapin sabun lo...**")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                        ytstreamlink = f['url']
                ytstream = ytstreamlink
            except Exception as e:
                await msg.edit(f"❌ **yah Eror kek otaklo !** \n\n`{e}`")
                return
            await sleep(2)
            try:
                chat_id = m.chat.id
                group_call = group_call_factory.get_group_call()
                await group_call.join(chat_id)
                await group_call.start_video(ytstream, repeat=False)
                VIDEO_CALL[chat_id] = group_call
                await msg.edit((f"💡 **started [youtube streaming]({ytstream}) !\n\n» join to video chat to watch the youtube stream.**"), disable_web_page_preview=True)
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"❌ **something went wrong!** \n\nError: `{e}`")
        else:
            await msg.edit("🔄 **jangan lupa siapin sabun lo ya mek...**")
            livestream = query
            chat_id = m.chat.id
            await sleep(2)
            try:
                group_call = group_call_factory.get_group_call()
                await group_call.join(chat_id)
                await group_call.start_video(livestream, repeat=False)
                VIDEO_CALL[chat_id] = group_call
                await msg.edit((f"💡 **started [live streaming]({livestream}) !\n\n» join to video chat to watch the live stream.**"), disable_web_page_preview=True)
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"❌ **ada masalah apasihh NGENTOD!** \n\nerror: `{e}`")

    elif media.video or media.document:
        msg = await m.reply_text("📥 **download bokep dulu hehe...**\n\n💭 __SABAR YA NGENTOD ANAK HARAM ANAK DAJJAL, TUNGGU AMPE SELESAI!.__")
        video = await media.download()
        chat_id = m.chat.id
        await sleep(2)
        try:
            group_call = group_call_factory.get_group_call()
            await group_call.join(chat_id)
            await group_call.start_video(video, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.edit("💡 **video dimulai jangan lupa siapin sabun!**\n\n» **naik ke vcg/os kalo mau nonton ya kontol.**")
            try:
                STREAM.remove(0)
            except:
                pass
            try:
                STREAM.add(1)
            except:
                pass
        except Exception as e:
            await msg.edit(f"❌ **yah si ngentod gangguan!** \n\nerror: `{e}`")
    else:
        await msg.edit("🔺 **tolong replay link youtub ya njing jangan film biru !**")
        return


@Client.on_message(command(["vstop", f"vstop@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def vstop(_, m: Message):
    chat_id = m.chat.id
    if 0 in STREAM:
        await m.reply_text("😕 **no active streaming at this time**\n\n» mulai film lu kontol /vstream command (reply to video/yt url/live url)")
        return
    try:
        await VIDEO_CALL[chat_id].stop()
        await m.reply_text("🔴 **bubar bubar raimu asu cok !**\n\n✅ __film udah selesai silahkan lap peju lo ya anj__")
        try:
            STREAM.remove(1)
        except:
            pass
        try:
            STREAM.add(0)
        except:
            pass
    except Exception as e:
        await m.reply_text(f"❌ **maaf eror kontol!** \n\nerror: `{e}`")
