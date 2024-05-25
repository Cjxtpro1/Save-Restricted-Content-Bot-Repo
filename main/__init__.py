#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = 22789024
API_HASH = "05dd73c56053828044cb71216cdfd0cc"
BOT_TOKEN = "6548950876:AAHNOrnrodvniHVpKB9rfbQrB-0bhX4eOkQ"
SESSION = "BQA29ZnSVsIYyA0W4n0iUPXkWeQLdvxzk9nlFSgM9UoelnosGbuLPUFw6RsLhiX7cJ1cvG0WgjSVYNJLHFZKZuVQHpTbj-P5Km3hb6wxp14M0LnTC2pUDVgcSlY5tD6rK-ht3AT0_2mQ6NLpI-7KwLdhtWjMLuj9XIAZspmk5mT2rmu_8goHZbKZj3UMg9aCtX_0SdNBvtI04oUT7fSm92SrEf3SbMvJrQ_k0EuP71b3Dgnl4zD_hUL8cTnfyhaJT9bXM64FsCI7IcOrCPx-axnC6YYPZDEfIsCiCIw7hBmJLtK6wxKd0R0FLNSfIJEPtUZgKyPXvHgzdWRCIG7pGKFZAAAAAZTVflsA"
FORCESUB = "bottgod"
AUTH = "6791986779"
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
