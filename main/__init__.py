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
SESSION = "BQBLQ8AsSVyGrwliZmhwDzOyKHI-CWI-eXfvY2DCR3WreDHn1-GRvPrIa-NNZ5rILxNOuQr-nNdyd8kiEwU5oCpoe64hZapXkDaifp4BK1FK9i6M9g8_Ffnbr54QcqgKjHvfRZFoDNNBEs4nw8ubm2DUm1cnQjb5wADJY5GrCNpLrVt9ay9E-Rc3zSOwabb2Qc0OuigulowOaUA3gmpkUOIi4DkcI1DEUzb_MuDVa5XtnQCC6APjJ-t_a_7EoL_HmKf87sDIHgAI5aRud41HbuNqqo-kECXo_lpq-q56KLKudKtc8barHOZKoPTDDGoRQixGPRKie4TB0ye5gLPjTaH8AAAAAZTVflsA"
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
