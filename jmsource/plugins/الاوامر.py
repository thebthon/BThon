from .. import *


@jmsource.ar_cmd(pattern="الاوامر")
async def hi(event):
    await edit_or_reply(
        event,
       "**[قنـاة السـورس ](t.me/BThon)\n✦┅━╍━╍╍━━╍━━╍━┅✦**\n\n**-  مرحبا بك عزيز المستخدم هذه هي قائمة اوامر سورس بيثون\n\n`.الامر1` ◂ اوامر الأدمن\n`.الامر2` ◂ اوامر المجموعة\n`.م3` ◂ اوامر الترحيب\n`.م4` ◂ اوامر الردود\n`.م5` ◂ اوامر الترفيه\n`.م6` ◂ اوامر حماية الخاص\n`.م7` ◂ اوامر الاذاعه و الكشف \n`.م8` ◂ اوامر البوت \n`.م9` ◂ اوامر المنع والترجمه\n`.م10` ◂ اوامر التلكراف و النطق\n`.م11` ◂ اوامر التحميل\n`.م12` ◂ اوامر التكرار\n`.م13` ◂ اوامر الانتحال والتقليد\n`.م14` ◂ اوامر الوقتي \n`.م15` ◂ اوامر الذاتيه والاضافه\n`.م16` ◂ اوامر البروفايل\n`.م17` ◂ اوامر الأكسترا\n`.م18` ◂ التاك و الملفات\n`.م19` ◂ اوامر الصيغ\n`.م20` ◂ اوامر التسلية\n`.م21` ◂ اوامر التحكم\n`.م22` ◂ اوامر حماية المجموعة \n`.م23` ◂ اوامر التجميع**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="الامر1")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الادمن : \n◂  `.حظر` \n❃ لحظر الشخص في مجموعه بالرد عليه\n\n ◂  `.الصورة -حذف`\n❃ اكتب الامر في المجموعة لحذف صورتها\n\n ◂  `.الصورة -وضع`\n❃ بالرد على الصورة في المجموعة لوضعها صورة للكروب\n\n ◂  `.الغاء الحظر`\n❃ لالغاء حظر الشخص من المجموعه بالرد عليه\n\n ◂  `.كتم` \n❃ لكتم الشخص بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.الغاء كتم`\n❃ لالغاء كتم الشخص بالرد عليه بالامر\n\n ◂  `.تثبيت` \n❃ بالرد على الرسالة لتثبيتها في المجموعة\n\n ◂  `.الغاء تثبيت` \n❃ لألغاء تثبيت الرسالة في المجموعة , اذا اردت الغاء تثبيت جميع الرسائل اكتب مع الامر الكل\n\n ◂  `.رفع مشرف`  < لقب > \n❃ بالرد ؏ المستخدم لرفعه مشرف يمكنك وضع لقب\n\n ◂  `.تنزيل مشرف` \n❃ بالرد ؏ المستخدم لتنزيله من المشرفين\n\n ◂  `.ارفع`\n❃ بالرد ؏ المستخدم لرفعه مشرف في جميع المجموعات \n\n ◂  `.نزل`\n❃ بالرد ؏ المستخدم لتنزيله من جميع المجموعات\n\n ◂  `.الاحداث`\n❃ فقط ارسل الامر لعرض اخر احداث المجموعه \n\n ◂  `.الغاء المحظورين`\n❃ لالغاء جميع المحظورين في المجموعه فقط اكتب الامر\n\n ◂  `.المحذوفين`\n❃ لعرض الحسابات المحذوفة في المجموعه فقط اكتب الامر\n\n ◂  `.تفليش`\n❃ لحظر جميع المستخدمين من المجموعه فقط اكتب الامر\n\n ◂  `.تنزيل الكل`\n❃ لتنزيل جميع المشرفين من المجموعه فقط ارسل الامر في المجموعه\n\n ◂  `.المحظورين`\n❃ لعرض المستخدمين المحظورين في المجموعه اكتب الامر فقط\n\n ◂  `.تحذير`\n❃ بالرد على المستخدم لتحذيره في المجموعه \n\n ◂  `.حذف التحذيرات`\nلحذف تحذيرات المستخدم بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.التحذيرات`\n❃ بالرد على المستخدم لعرض عدد تحذيراته**",
    )


@jmsource.ar_cmd(pattern="الامر2")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر المجموعة :\n\n ◂  `.المشرفين` \n❃ فقط اكتب الامر في المجموعه لعرض مشرفين المجموعه\n\n ◂  `.البوتات` \n❃ فقط اكتب الامر في الدردشة لعرض البوتات المضافة \n\n ◂  `.الاعضاء`\n❃ فقط اكتب الامر في المجموعه لعرض أعضاء الدردشة\n\n ◂  `.معلومات`\n❃ لعرض معلومات المجموعه اكتبه الامر في المجموعة**",
    )


@jmsource.ar_cmd(pattern="م3")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر الترحيب :\n\n ◂  `.ترحيب`\n❃ اكتب الامر مع الترحيب ليقوم بالترحيب في المستخدمين الجدد في المجموعة\n\n ◂  `.الترحيب`\n❃ لعرض رساله الترحيب الحاليه اكتب الامر فقط\n\n ◂  `.حذف الترحيب`\n❃ لالغاء الترحيب في المستخدمين فقط اكتب الامر\n\n⌔∮ متغيرات الترحيب [اضغط هنا](https://t.me/Vars_BT)**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م4")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر الردود :\n\n ◂  `.رد`\n❃ يستخدم الأمر بإضافة رد في المجموعه اكتب الامر والرد الخاص بك بالرد على الكلمه \n\n ◂  `.حذف الردود`\n❃ فقط اكتب الامر في الدردشه لحذف جميع الردود المضافه\n\n ◂  `.الردود`\n❃ لعرض الردود المصافه فقط اكتب الامر\n\n ◂  `.ايقاف`\n❃ اكتب الامر مع الرد لحذف الرد من الدردشه\n\n⌔∮ شرح توضيحي عن اوامر الردود  [اضغط هنا](https://graph.org/اوامر-بيثون-04-24)\n⌔∮ شرح عن متغيرات الردود  [اضغط هنا](https://t.me/Vars_BT)**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م5")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الترفيه:**\n\n جميع هذه الاوامر تستخدم بالرد على الشخص كترفيه\n ◂  `.رفع مطي`\n ◂  `.رفع كلب`\n ◂  `.رفع حيوان`\n ◂  `.رفع زاحف`\n ◂  `.رفع مرتي`\n ◂  `.رفع زوجي`\n ◂  `.رفع تاج`\n ◂  `.رفع بكلبي`\n ◂  `.رفع بزون`\n ◂  `.رفع قرد`\n\n ◂  `.نسبة الحب`\n ◂  `.نسبة الانوثة`\n ◂  `.نسبة الرجولة`\n ◂  `.نسبة الغباء`\n ◂  `.نسبة المثْلية`\n\n ◂  `.كت`\n ◂  `.اوصف`\n ◂  `.هينه`\n ◂  `.نزوج`\n ◂  `.طلاك`",
    )


@jmsource.ar_cmd(pattern="م6")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر حماية الخاص :\n\n ◂  `.الحماية تشغيل`\n❃ لتشغيل امر الحمايه يستخدم لتحذير المستخدمين عند مراسلتك في الخاص من التكرار\n\n ◂  `.الحماية تعطيل`\n❃ لتعطيل امر الحمايه وعدم تحذير المستخدمين في الخاص\n\n ◂  `.سماح` او `.س`\n❃ يستخدم الامر لقبول الشخص في الخاص وعدم ارسال تحذيرات له بالرد على الشخص\n\n ◂  `.رفض` او `.ر`\n❃ يستخدم لرفض الشخص من الخاص وتحذيره اذا كرر الرسائل وبعدها حظره\n\n ◂  `.بلوك`\n❃ بالرد على المستخدم لحظره من الخاص\n\n ◂  `.انبلوك`\n❃ بالرد على المستخدم لالغاء حظره من الخاص\n\n ◂  `.المسموح لهم`\n❃ اكتب الامر فقط لعرض معلومات عن الاشخاص الذين قبلته في الخاص\n\n⌔∮ لعرض فارات الحماية ارسل `.الفارات`**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م7")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر الكشف والاذاعة  :\n\n ◂  `.ايدي`\n❃ بالرد على المستخدم او وضع معرفه مع الامر لعرض معلوماته\n\n ◂  `.كشف`\n❃ بالرد على المستخدم لعرض معلومات معينه عنه\n\n ◂  `.للخاص`\n❃ اكتب الامر بالرد على رساله او اي ميديا ليقوم بارساله لجميع المحادثات في الخاص\n\n ◂  `.للكروبات`\n❃ بالرد على نص او اي ميديا ليقوم بنشره في جمبع المجموعات\n\n⌔∮ متغيرات الايدي  [اضغط هنا](https://t.me/Vars_BT)**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م8")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر البوت :\n\n ◂  `.فحص`\n❃ فقط اكتب الامر لعرض معلومات السورس\n\n ◂  `.بنك`\n❃ فقط اكتب الامر لعرض سرعه البوت\n\n ◂  `.الانترنت + الاضافه`\n❃ يستخدم الامر لقياس سرعه البوت اكتب الامر مع الاضافه  :  `.الانترنت صورة`  `.الانترنت نص`\n\n ◂  `.اعادة تشغيل`\n❃ لعمل اعادة تشغيل للسورس وتحديثه \n\n ◂  `.الاشعارات` + تشغيل/تعطيل\n❃ لتشغيل او تعطيل الاشعارات عند تحديث او اعادة تشغيل السورس**",
    )


@jmsource.ar_cmd(pattern="م9")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر المنع والترجمة :\n\n ◂  `.منع`\n❃ اكتب الاكر مع الكلمه لمنع ارساله في المجموعه او اي دردشه\n\n ◂  `.الغاء منع`\n❃ اكتب الامر مع الكلمه لالغاء منعها من الدردشه\n\n ◂  `.قائمة المنع`\n❃ اكتب الامر لعرض قائمه الكلمات التي منعتها في الدردشة\n\n ◂  `.ترجمة`\n❃ يستخدم الاكر لترجمه الكلمات اكتب الامر مع كود اللغه بالرد غلى النص لترجمته\n\n⌔∮ اكواد اللغات للترجمه  [اضغط هنا](https://graph.org/اكواد-اللغه-للترجمه-04-24)**",
    )


@jmsource.ar_cmd(pattern="م10")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر التلكراف و النطق :\n\n ◂  `.انطق`\n❃ بالرد على الكلام لتسجيله ببصمه و ارساله لك\n\n ◂  `.تلكراف ميديا ◂  \n❃ بالرد على الميديا لصنع رابط تلكراف منها\n\n ◂  `.تلكراف نص`\n❃ بالرد على النص لعمل رابط تلكراف**",
    )


@jmsource.ar_cmd(pattern="م11")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائمـه اوامر التحميل :\n\n ◂  `.متحركات`\n❃ بكتابة عنوان مع الامر لجلب متحركة لك من العنوان\n\n ◂  `.فلم`\n❃ بكتابة اسم الفلم باللغة الانجليزية مع الامر لعرض معلومات الفلم\n\n ◂  `.تحميل فيديو`\n❃ بالرد على رابط من يوتيوب او اي موقع ثاني لتحميل الفيديو وارساله لك\n\n ◂  `.تحميل صوتي`\n❃ اكتب الامر بالرد على الرابط من اليوتيوب لتكميل مقطع الصوتي و ارساله لك\n\n ◂  `.انستا`\n❃ اكتب الامر بالرد على الرابط التحميل من الانستا \n\n ◂  `.بينترست`\n❃ بالرد على رابط من بينتسرت للتحميل لك\n\n ◂  `.صور`\n❃ اكتب الامر مع عنوان للبحث عنه وارسال لك الصور،  اذا بحثت عن اباحي سيتم تعطيل حسابك**",
    )


@jmsource.ar_cmd(pattern="م12")
async def hi(event):
    await edit_or_reply(
        event,
        "** قائـمه اوامر التكرار**:\n\n ** `.كرر`\n❃ اكتب الامر مع عدد التكرار بالرد ؏ النص او او صورة ملصق ليقوم بتكراره مع العدد الذي وضعته\n\n ◂  `.تكرار الملصق` \n❃ بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها في الدردشة\n\n ◂ `.مكرر`\n❃ اكتب الامر مع وقت بالثواني و مع عدد التكرار وبالرد على صورة او نص  (  تكرار وقتي  )\n\n ◂  `.التكرار`\n❃ بالرد على الرسالة بالامر فقط سيقوم بعمل تكرار سريع ويصل عدده الى 10 الاف تكرار  ! \n\n ◂  `.ايقاف التكرار`\n❃ يقوم هذا الامر بأيقاف التكرار فقط اكتبه\n\n تنبيه اوامر التكرار قد تؤدي الى حظر حسابك على التلي اذا استخدمتها بشكل غير صحيح**",
    )


@jmsource.ar_cmd(pattern="م13")
async def hi(event):
    await edit_or_reply(
        event,
        "** قائـمه اوامر الأنتحال و التقليد :**\n\n ◂  ** `.انتحال`\n❃ بالرد على المستخدم لأنتحال حسابه  من اسم وصورة وبايو  . \n\n ◂  `.اعادة الحساب`\n❃ لأعادة حسابك الى وضعه السابق  .\n\n ◂ `.تقليد`\n❃ بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n ◂ `.الغاء تقليد`\n❃ بالرد على الشخص لايقاف التقليد\n\n ◂ `.المقلدهم `\n❃ لاظهار قائمه الاشخاص الذي فعلت عليهم امر التقليد ولمسحهم ارسل  `.حذف المقلدهم` **",
    )


@jmsource.ar_cmd(pattern="م14")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الوقتي:**\n\n◂ `.اسم وقتي`\n❃ بكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها \n\n ◂ `.انهاء اسم وقتي`\n❃ لانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n ◂ `.بايو وقتي`\n❃ بكتابة الامر لاضافة ساعه يتحرك مع النبذة الخاصة بك  \n\n ◂ `.انهاء بايو وقتي`\n❃ لانهاء البايو الوقتي و ارجاع البايو الطبيعي\n\n ◂  `.الصورة الوقتية`\n❃ لبدء تشغيل وقت على الصورة الخاصة بحسابك\n\n ◂  `.انهاء الصورة الوقتية`\n❃ لألغاء امر الصورة الوقتية**",
    )


@jmsource.ar_cmd(pattern="م15")
async def hi(event):
    await edit_or_reply(
        event,
        "**اوامر جلب الذاتية وامر الاضافة**:\n\n ◂  `.ضيف`\n❃ اكتب الامر مع رابط مجموعه التي تريد سحب اعضائها وارسل الامر في مجموعتك لسحبهم الى مجموعتك\n\n ◂ `.جلب الصورة`  او  `.ذاتية`\n❃ بالرد على صورة او فيديو ذاتية التدمير لحفظها وارسالها في الرسائل المحفوظة بسرية تامة الامر لبيثون حصريا!**",
    )


@jmsource.ar_cmd(pattern="م16")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر البروفايل: \n\n ◂  `.تغيير اسم`\n❃ لتغيير اسم حسابك اكتب الاسم مع الامر\n\n ◂  `.تغيير بايو`\n❃ لتغيير بايو حسابك اكتب البايو مع الامر \n\n ◂  `.تغيير صورة`\n❃ لتغيير صورة حسابك بالرد على الصورة بالامر\n\n ◂  `.تغيير معرف`\n❃ لتغيير معرف حسابك اكتب المعرف مع الامر\n\n ◂  `.ازالة الصورة`\n❃ اكبت الامر لحذف صورة حسابك\n\n ◂  `.معرفاتي`\n❃ لعرض معرفات حسابك التي صنعتها\n\n ◂  `.حسابي`\n❃ لعرض معلومات و احصائيات حسابك**",
    )


@jmsource.ar_cmd(pattern="م17")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الأكسترا: \n\n ◂  `.فك المحظورين`\n❃ قم بكتابة الامر لفك جميع المستخدمين الذي حظرتهم من الخاص\n\n ◂  `.وهمي كتابه`\n❃ لبدء وضع كتابة بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي فيديو`\n❃ لبدء وضع ارسال فيديو بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي لعبه`\n❃ لبدء وضع ارسال لعبة بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي صوتي`\n❃ لبدء وضع ارسال بصمة صوتية بشكل وهمي جربه بنفسك\n\n ◂  `.الحاسبة`\n❃ لعرض حاسبه علميه جربه بنفسك\n\n ◂  `.حالتي`\n❃ لعرض حاله حسابك الحاليه اذا كان محظور او لا\n\n ◂  `.صلاة`❃ اكتب الامر مع اسم محافظتك او مدينتك بالانكليزي لعرض اوقات الصلاة والامساك\n\n ◂  `.تغميق`\n❃ بالرد على الكلام لجعله بشكل غامق\n\n ◂  `.نسخ`\n❃ بالرد على الكلام لجعله بشكل للنسخ\n\n ◂  `.مائل`\n❃ بالرد على الكلام لجعله بشكل مائل**",
    )


@jmsource.ar_cmd(pattern="م18")
async def hi(event):
    await edit_or_reply(
        event,
        "قائـمه اوامر التاك والملفات:\n\n ◂  او  `.تاك للكل`\n❃ لعمل تاك لاخر 100 عضو في المجموعه اكتب الامر مع اي نص تريد\n\n ◂  `.تبليغ`\n❃ لتبليغ المشرفين اذا حصل شيء ما فقط اكتب الامر\n\n ◂  `.منشن`\n❃ بالرد على المستخدم وكتابه شيء مع الامر لعمل تاك داخل الكلمه للمستخدم\n\n ◂  `.تنصيب`\n❃ لتنصيب ملفات خارجيه للسورس \n\n ◂  `.الغاء تنصيب`\n❃ بكتابه الامر مع اسم الملف لحذف تنصيبه من السورس",
    )


@jmsource.ar_cmd(pattern="م19")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الصيغ:\n\n ◂  `.فاس`\n❃ بالرد على متحركو او فيديو لتحويله الى ملصق متحرك\n\n ◂  `.تحويل صورة`\n❃ بالرد على ملصق اتحويله الى صورة\n\n ◂  `.تحويل ملصق`\n❃ بالرد على الصورة لتحويلها الى ملصق\n\n ◂  `.تحويل متحركة `\n❃ بالرد على الفيديو لتحويله الى متحركة \n\n◂  `.لملف`\n❃ بكتابة اسم الملف والرد على كتابة لتحويلها الى ملف\n\n ◂  `.لكتابة`\n❃ بالرد على الملف لاستخراج النص الذي بداخله وارساله لك\n\n ◂  `.الملف لصورة`\n❃ بالرد على الصورة التي تكون بشكل ملف لتحويلها لصورة عادية\n\n ◂  `.تحويل بصمة`\n❃ بالرد على المقطع الوصتي لتحويله الى بصمة\n\n ◂  `.تحويل صوتي`\n❃ بالرد على البصمة لتحويلها على شكل مقطع صوتي**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م20")
async def hi(event):
    await edit_or_reply(
        event,
        "**⌔∮ قائـمة اوامر التسلية**: \n\n** `.غبي`  `.القنابل`  `.اتصل`   `.قتل`    `.طوبة`\n\n`.مربعات`   `.حلويات`     `.نار`     `.شحن`\n\n`.افكر`    `.متت`    `.ضايج`    `.ساعة`\n\n`.مح`    `.قلب`     `.جيم`     `.الارض`\n\n`.قمر`      `.اقمار`     `.قمور `    `.نجمه`\n\n`.مكعبات`   `.مطر `     `.تفريغ`      `.فليم`\n\n`.احبك`    `.طائره`        `.شرطه `\n\n`.النضام الشمسي`    `.قاتل`       `.عين`\n\n`.افكرر`      `.افعى`         `.رج`      `.مايكرو`\n\n`.فايروس`    `.قطار`      `.موسيقى `\n\n`.رسم`   `.تحميل`     `.مربع`       `.دائره`\n\n`.انيم`    `.بشره`      `.قرد`      `.يد`\n\n`.العد التنازلي`        `.قلوب`\n\n`.فصخ + الكلام`\n\n`.تهكير`     `.تهكير2`   `.تهكير3`\n\nٴ╼──────────────────╾\n • جميع الاوامر تستخدم بالضغط على الامر راح ينسخ وحده وارسله فقط **",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م21")
async def we(event):
    await edit_or_reply(
        event,
        "**[قنـاة السـورس ](t.me/BThon)**\n✦┅━╍━╍╍━━╍━━╍━┅✦\n\n• **اوامر التحكم تتيح لمستخدم اخر ان يستخدم اوامر تنصيبك وهو غير منصب بيثون حيث سيصبح متحكم في اوامر تنصيبك يرجى الانتباه من انه سيحصل على صلاحيات الاوامر وقد يسبب خطورة لك اذا كنت لا تثق في المستخدم الذي اضفته. \n\n\n`.التحكم` تفعيل/تعطيل\n• تستخدم هذه الميزة لتفعيل/لتعطيل خاصية التحكم بأوامر تنصيبك للمستخدمين الذين أضفتهم في قائمة المتحكمين\n\n`.المتحكمين`\n• لعرض المستخدمين الذين اضفتهم الى قائمة المستخدمين المتحكمين\n\n`.اضف متحكم`\n• بالرد على المستخدم لأضافته متحكم في تنصيب بيثون الخاص بك\n\n`.ازالة متحكم`\n• بالرد على المستخدم لازالته من قائمة المتحكمين**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م22")
async def ae(event):
    await edit_or_reply(
        event,
        "**[قنـاة السـورس ](t.me/BThon)**\n✦┅━╍━╍╍━━╍━━╍━┅✦\n\n• **اوامر حماية المجموعات بالمسح والتحذير\n\n ◂  `.قفل/فتح`\nالسب\nالفارسية\nالميديا\nالبوتات\nالدخول\nالاضافة\nالتوجيه\nالروابط\nالمعرفات\nالكل\n\n• فقط عليك كتابة قفل او فتح مع الاضافة لقفلها ولأظهار الصلاحيات ارسل `.الاعدادات`\n\n ◂  `.البوتات`\n•لمعرفة البوتات في المجموعة ولطردهم**",
        link_preview=False,
    )


@jmsource.ar_cmd(pattern="م23")
async def ae(event):
    await edit_or_reply(
        event,
        "**[قنـاة السـورس ](t.me/BThon)**\n✦┅━╍━╍╍━━╍━━╍━┅✦\n\n• ** قائمة اوامر التجميع سيتم تحديث القائمة لاحقًا ** ",
        link_preview=False,
    )
