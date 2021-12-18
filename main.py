import random, re
from uniborg.util import all_cmd
import asyncio
from telethon import events
import os
import telebot



bot=telebot.TeleBot('5092293428:AAEViJbsdhTHIqcLU_WZNr_v-U3cB8DqKdQ')

@borg.on(pattern="start ?(/*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😒You Know I'm a good **BOT**😏")
        await asyncio.sleep(1.9)
        await event.edit("BUT😡")
        await asyncio.sleep(1.2)
        await event.edit("😑Don't give me a reason😠")
        await asyncio.sleep(1.9)
        await event.edit("🤨To show my😎")
        await asyncio.sleep(1.4)
        await event.edit("**😈DEVIL SIDE**😈")
        await asyncio.sleep(1.3)
        await event.edit("**😈YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY DEVIL SIDE😂**")
        await asyncio.sleep(2.1)
        await event.edit("**👿🇱🇰 Im WhiteDevil's Assistant Bot 👿🇱🇰**")








