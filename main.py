import asyncio

from pyrogram import Client
from pyrogram import types, filters
from sqlalchemy.ext.asyncio import AsyncSession

from config import api_id, api_hash, FROM_CHANNEL_ID, BOT_ID
from db.get_names import get_manhva_names
from db.base import create_session


app = Client(
    'new_acc',
    api_id=api_id,
    api_hash=api_hash
)


@app.on_message()
async def my_handler(client: Client, message: types.Message):
    if message.chat.id == FROM_CHANNEL_ID and message.text.split('\n', maxsplit=1)[0] in manhva_names.get_names():
        text = f'/newchitka {message.text}'
        await client.send_message(chat_id=BOT_ID, text=text)
    elif message.chat.id == BOT_ID:
        async with create_session() as session:
            await manhva_names.refresh_list(session=session)
    elif message.chat.id == 1835906223 and message.text == 'list':
        print(manhva_names.get_names())
    elif message.chat.id == 1835906223:
        text = message.text.split('\n', maxsplit=1)[0]
        await client.send_message(chat_id=1835906223, text=text)
    else:
        return


class ManhvaName:
    __manhva_names = []

    async def refresh_list(self, session: AsyncSession):
        self.__manhva_names = await get_manhva_names(session=session)

    def get_names(self):
        return self.__manhva_names

manhva_names = ManhvaName()


async def main():
    async with create_session() as session:
        await manhva_names.refresh_list(session=session)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    print(manhva_names.get_names())
    app.run()
