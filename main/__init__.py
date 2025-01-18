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
API_ID = 23147177
API_HASH = "6c1b34bf3c56b9957aab7da8a0dd3482"
BOT_TOKEN = "8096714394:AAEUc0ewpR-vmAe7V_1z-g9yLkx93cN3JPU"
SESSION = "BQBGSMnsR5TFL3VM9QxSctLRlR8AH_enTsC6gnJfCa61-570UZAZzPxEFluH2w0tNsfrzRanQDExLZwyrmbQKuKPYwl7pm7ChE5eNZ5FaGy_xVxGmnMoZI9AB6Kg0PumU8ntoWWxo1hVJ5L28lhUiT_s9f3-RI9NI6aMFb_dpQ9eBKiU3MRPAYNs1ROExtsg6cdnM32vwunBMCU5voamTdieLRjgGvK-vBvyKLUdhI4U3_gvHcLz6DqcBoBzsVQOJ2dJ0BElbm_oy62Au0-WeXHyl6T2qdB3t-H671CJgn77ZM4siNFr6FeVl5bNpLPcbPOcFCJ-wQi3AjXgbqC_MCRMAAAAAYno6LkA"
FORCESUB = "savebotuser2"
AUTH = "6608709817"
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
