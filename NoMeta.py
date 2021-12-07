"""
    Copyright 2021 t.me/innocoffee
    Licensed under the Apache License, Version 2.0
    
    Author is not responsible for any consequencies caused by using this
    software or any of its parts. If you have any questions or wishes, feel
    free to contact Dan by sending pm to @innocoffee_alt.
"""

#<3 title: NoMeta
#<3 pic: https://img.icons8.com/fluency/50/000000/v-live.png
#<3 desc: Отключает уведомления и вразумляет людей не писать "Привет, Hi" и др.

from .. import loader, utils

@loader.tds
class NoMetaMod(loader.Module):
    """Отключает уведомления и вразумляет людей не писать "Привет, Hi" и др. Сделал только для лс, изменил текст, добавил русский язык @Friendly_userbot - @ForceBrain"""

    strings = {
        "name": "NoMeta",
        "no_meta": "<b>@Loner2000 system</b> \n🇺🇸  I will answer you when I am <b>free</b>. \n🇷🇺 Отвечу вам когда <b>освобожусь</b>."
    }

    async def client_ready(self, client, db):
        self.client = client

    async def nometacmd(self, message):
        """Если кто-то отправил мету по типу 'Привет', эта команда его вразумит"""
        await self.client.send_message(message.peer_id, self.strings('no_meta'), reply_to=getattr(message, 'reply_to_msg_id', None))
        await message.delete()

    async def watcher(self, message):
        try:
            text = message.raw_text
        except:
            return

        meta = [
            'прив', 'привет', 'салют', 'алоха', 'hi', 'hello', 'хелло', 'хеллоу', 'хэллоу', 'коничива', 'konichiwa', 'ку',
            'ку ку', 'хай', 'хей', 'хэй', 'hey', 'hey there', 'слушай', 'слуш', 'слыш', 'о', 'м?', 'а?', 'йо', 'yo', 'йоу', 'ара',
            'артур', 'арик', 'q', 'qq', 'брад', 'волчонок', 'волк',  'здравствуйте', 'здравствуй', 'здорова', 'салом', 'salom', 'брат', 'крч', 'короче', 'тут',
            'тут?', 'слушай', 'блин', 'блять', 'бля', 'браин', 'что с браином?', 'надо', 'это', 'дело', 'ты мне нужен',
            'ты мне нужен срочно', 'помоги', 'у меня', 'сделай', 'привет есть минутка?', 'привет, есть минутка?',
            'привет. есть минутка?', 'есть минутка?'
        ]

        if message.raw_text.lower() in meta:
            try:
                if not message.is_private: return
                await self.client.send_message(message.peer_id, self.strings('no_meta'), reply_to=message.id)
                await self.client.send_read_acknowledge(message.chat_id, clear_mentions=True)
            except: pass