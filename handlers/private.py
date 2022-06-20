from sys import version_info
from handlers import __version__
from pyrogram import Client, filters, __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from helpers.dbchat import add_served_chat, is_served_chat
from helpers.dbpunish import is_gbanned_user
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from time import time
from datetime import datetime

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_NAME,
    UPDATES_CHANNEL,
    ASSISTANT_NAME,
)
from helpers.filters import command, other_filters2
#  


__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)




@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAI8bmKIvgnlJyCrq9HIxSvCZCbm5CEjAAIaEAACpvFxHg-Z648-SCRWJAQ")
    await message.reply_text(
        f"""**مرحبا {message.from_user.mention} 🎵\nانا {BOT_NAME}!\n
● **البوت الخاص بي الذي يمكنه تشغيل الموسيقى في الدردشات الصوتية.**

● ** الحظر غير المصرح به ، ومنح إذن إدارة المحادثه المرئية وإضافة المساعد إلى المجموعة.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕اصفني الي مجموعتك➕", 
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 الحساب المساعد", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 جروب الدعم", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 الاوامر" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 قناه المطور", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ), 
    ) 
    
  
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🧸 {BOT_NAME} Online**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📣 جروب الدعم", url=f"https://t.me/{SUPPORT_GROUP}")]])
    )

@Client.on_message(filters.private & filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("❗ ملاحظة:يلزم وجود الأذونات الأربعة التالية لكي يعمل الروبوت بنشاط:- صلاحية حذف الرسائل ،- صلاحية الدعوة عن طريق الرابط ،- صلاحية إدارة الدردشة الصوتية.- إذن تثبيت الرسالة.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔓 اوامر الاعضاء", callback_data="herkes"), 

                     InlineKeyboardButton(
                         "🔐 اوامر الادمن", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "🧙‍♂️ اوامر المالك", callback_data="sudo")
                 ],[
                     InlineKeyboardButton(
                         "🏠 القائمة الرئيسية", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🪐 المطور", url=f"https://t.me/{OWNER_NAME}")
                 ]
             ]
         )
    )




@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ ملاحظة: \n الامتيازات الأربعة التالية مطلوبة لكي يعمل الروبوت بفاعلية: \n- صلاحية حذف الرسائل ، \n- دعوة بواسطة سلطة الارتباط ، \n- صلاحية إدارة الدردشة الصوتية. \n- صلاحية تثبيت الرسائل.", 
    reply_markup=InlineKeyboardMarkup(çalışması için şu dört yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.\n- Mesaj sabitleme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(

      [
        [
          InlineKeyboardButton(
            "🔓 اوامر الاعضاء", callback_data ="herkes"), 
          
          InlineKeyboardButton(
            "🔐 اوامر الادمن",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🧙‍♂️ اوامر المالك",callback_data ="sudo")
        ],
        [
          InlineKeyboardButton(
            "🏠القائمه الرئيسية", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🪐 المطور", url=f"https://t.me/{OWNER_NAME}")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!قائمة الأوامر لهذا الروبوت للجميع 💕

 ▶ ️ / play - الرد على رابط youtube أو ملف الأغنية لتشغيل الأغنية

 ▶ ️ / play - قم بتشغيل الأغنية التي تريدها

 🔴

 🎵 / اعثر - اعثر بسرعة على الأغاني التي تريدها

 🎵 / vbull اعثر بسرعة على مقاطع الفيديو التي تريدها

 🔍 / بحث - البحث في youtube عن مقاطع الفيديو بالتفاصيل

 🏓 / ping bot يتحقق من حالة ping eder\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 المطور", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ رجوع", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!قائمة الأوامر لهذا الروبوت للمسؤولين

 ▶ ️ / تابع - استمر في تشغيل الأغنية

 ⏸️ / stop - لإيقاف المسار الحالي مؤقتًا

 🔄 / تخطي- يتخطى المسار الموسيقي في قائمة الانتظار.

 ⏹ / النهاية - إيقاف تشغيل الموسيقى

 🔼 / ver تخويل المستخدم حتى يتمكن الروبوت من استخدام الأوامر المتاحة فقط للمسؤول

 🔽 / al امنح المستخدم الذي يمكنه استخدام أوامر إدارة الروبوت

 ⚪ / مساعد - ينضم مساعد الموسيقى إلى مجموعتك..\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 المطور", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ رجوع", callback_data="cbhelp")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("sudo"))
async def sudo(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!قائمة الأوامر للمالك لهذا الروبوت 👨‍💻

 »/ بث => بث!

 »/cast_pin => تثبيت البث في مجموعات!

 »/ gban => حظر !

 »/ ungban => رفع الحظر!

 »/ alive => يظهر حالة عمل الروبوت! \n\n</b""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 المطور", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ رجوع", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Merhaba şuan aktif olarak çalışmaktayım yardım için aşağıda buttonu kullanınız!**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Yardım", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **Merhaba {query.from_user.mention} 🎵\nBen {BOT_NAME}!\n\n● Sesli sohbetlerde müzik çalabilen botum.\n\n● Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕اضفني الي مجموعتك➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 الحساب المساعد", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 جروب الدعم", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 الاوامر" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 قناه المطور", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )

@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📣 جروب الدعم", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton(
                    "🗯️ قناه المطور", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**• ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()} {BOT_NAME}**\n\n🧑🏼‍💻 المطور: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n👾 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n🔥 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n🐍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n✨ PʏTɢCᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n🆙 ᴄᴀʟɪsᴍᴀ ᴅᴜʀᴜᴍᴜ: `{uptime}`\n\n❤ **Bᴇɴɪ ɢʀᴜʙᴀ ᴀʟᴅɪɢɪɴɪᴢ ɪᴄɪɴ ᴛᴇsᴇᴋᴋᴜʀʟᴇʀ . . !**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )




@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


chat_watcher_group = 5

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Yasaklı** kullanıcı algılandı, bu kullanıcı sudo kullanıcısı tarafından yasaklandı ve bu Sohbetten engellendi !\n\n🚫 **Sebep:** potansiyel spam ve suistimalci."
        )
