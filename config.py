#(©)NextGenBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5865768108:AAF6u52zavrIvUV1AjsJsjjqkxj6lx6ZUSzEeYKp0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9102574"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0861a545777adba2d599304b6474aad1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002642523721"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5053078995"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://nitesh:Ayush@cluster0.k1zk9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "techvjlink.site")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "0715e20af7c3a36853d2c90232e1f62954d17d92")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/Mrstrangemovie/21")


#force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002357822394"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002213098381"))
REQUEST_CHANNEL = int(os.environ.get("REQUEST_CHANNEL", "-1001853597187"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>👋👋 Hey {first} ! </b>\n\n<b> 𝐈'𝐦 𝐚 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭🤖...! </b>\n\n 𝐈 𝐂𝐚𝐧 <b> 𝐒𝐭𝐨𝐫𝐞 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐅𝐢𝐥𝐞𝐬</b>  𝐢𝐧 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐨𝐭𝐡𝐞𝐫 𝐮𝐬𝐞𝐫𝐬 𝐜𝐚𝐧 𝐚𝐜𝐜𝐞𝐬𝐬 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐅𝐢𝐥𝐞𝐬 𝐅𝐫𝐨𝐦 𝐚 𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐋𝐢𝐧𝐤....!\n\n⚡<b> 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 - </b>❝𝐌𝐨𝐯𝐢𝐞 𝐒𝐭𝐚𝐫❞")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1685470205 5212197608").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", " 𝐇𝐞𝐥𝐥𝐨 {first}\n\n<b> 𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐁𝐨𝐭𝐡  𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞\n\n 𝐊𝐢𝐧𝐝𝐥𝐲 𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</b>")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")
    
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We @top_hd_movies_official or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None)

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(5053078995)
ADMINS.append(5212197608)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
