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
BOT_TOKEN = "6548950876:AAH5kZenTHxuVfNmkhOr4Em0q3SomQK2LmQ"
SESSION = "BQAwMGlgss4vvyVDewEl0CfmlfNbNsz3duhHS6lJySs-ShKbiJhVAYfcbtyaXlIrajcQS6nHzCPOBtEpmFcwz1-daU6MsDRM5Mby75d2vd193RnspbZCgz1huj-Grddh18l9uNg7WUT8gWFY5iQ3D5ghvRtbgEflfC0vpE7qlOinxnYESlqGBXoyjt1HKdz3aXY-VGdMCI6bLFgk6vNcMgABSQY9D--8ck6vF5KqAShpABlvlYudRZpm5dV5E-Bq2DQbOflE_q3eYqYIvRgUQf8vYhrof8OgxsfnVY8gfbueE82FA8IyRewB2Y2dNSST6O04tEQN05ydT6hN2WSER3ZuAAAAAZTVflsA"
FORCESUB = "bottuse"
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
