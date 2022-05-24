# import logging
from pyrogram import Client, idle
api_id = 14266125
api_hash = "3f5db9ec965a20493539f979b1381791"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)

# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
