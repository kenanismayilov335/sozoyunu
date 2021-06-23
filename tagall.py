# Modul aykhan_s tərəfindən hazırlanıb
# Bu yazıları silməməy şərtiylə istədiyiniz 
# repoda istifadə edə bilərsiniz

import time
import requests
from collections import deque
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP, bot
from userbot.events import register
import telethon
from telethon import events


@register(outgoing=True, pattern="^.100$")
async def _(event):
    if event.fwd_from:
        return # @yusiqo
    mentions = "@100"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    



