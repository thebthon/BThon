#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
# حقوق و كتابة الملف تتبع الى سورس زدثون
#to update BThon

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jmsource import jmsource

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


@jmsource.ar_cmd(
    pattern="تيكتوك(?:\s|$)([\s\S]*)",
    command=("تيكتوك", plugin_category),
    info={
        "header": "لـ تحميل الفيـديـو من تيـك تـوك عبـر الرابـط",
        "الاستـخـدام": "{tr}تيكتوك بالـرد ع رابـط",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**``` بالـرد على الرابـط ```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط ```**")
        return
    chat = "@CGBOT"
    jmthonevent = await edit_or_reply(event, "** جـارِ التحميـل من تيـك تـوك انتظـر قليلاً  ... **")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2035595446)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await jmthonevent.edit(
                "**تحـقق من انـك لم تقـم بحظـر البوت @CGBOT .. ثم اعـد استخدام الامـر ...**"
            )
            return
        if response.text.startswith(""):
            await jmthonevent.edit("**🤨💔...؟**")
        else:
            await jmthonevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "تيك توك": "**اسم الاضافـه : **`تيك توك`\
    \n\n** الامـر ⦂ **`.تيكتوك` بالرد على الرابط\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من تيـك تـوك"
    }
)
