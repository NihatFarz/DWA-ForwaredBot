from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Başladılır...")

# Əsaslar
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    Farz = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    Farz.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@Farz.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await Farz.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot İşləkdir.")
Farz.run_until_disconnected()
