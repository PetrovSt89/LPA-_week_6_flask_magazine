import time

from telethon import TelegramClient
from config import api_id, api_hash

api_id = api_id
api_hash = api_hash


client = TelegramClient(session='test_tg', api_id=api_id, api_hash=api_hash)

def main():
    # me = await client.get_me()
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        if dialog.title == '🏐 Пескоструйка 💦':
            messages = client.iter_messages(dialog)
            for message in messages:
                print(message.text)
                time.sleep(1)
with client:
    client.loop.run_until_complete(future=main())