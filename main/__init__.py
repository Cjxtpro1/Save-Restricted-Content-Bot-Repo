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
SESSION = "BQFhMqkAs0UeozF4ByfBuxI8aFFyzvVzTMwzckBv2pLGMaiOYFCljurlF1OP0xgHOtjdT1SVbUMNX-BuPKQd6Ij4oPWfAiUwV17pBrEVgHPqhicoadT7GjVFWLBYa8F_Mg6865qeUHnQjywhoyEypATINdDo48YRb57jUUUUcN2oMwPINJ757K5o9RH70yxLlXvoVOqePzciDp0esFWQ6vi9zZWEvP4Z_PcGT9ISzQh7hG4HXpbCw_7PGF_qHyYdnxWlnFKP6BXjdsZCah0g-ZfVG-qjzHjK18zqc-MVWpiyFdwWpChxEBKQcJkffJw7WgvNlV3Y711m0z3-_vrzrM2NjFnhwgAAAAGJ6Oi5AA"
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
