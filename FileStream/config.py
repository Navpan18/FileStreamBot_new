from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int('20295350')
    API_HASH = str('805a0a86f3b382d904617d0a2fd4fb6f')
    BOT_TOKEN = str('6860327887:AAGTxyHUBY3F9nZvgC0rs0F0jSD8GqvI2r8')
    OWNER_ID = int('1220356966')
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str('mongodb+srv://Navpan:Ramnagar@telegrambot2.5aga6dx.mongodb.net/?retryWrites=true&w=majority')
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_UPDATES_CHANNEL = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    IMAGE_FILEID = env.get('IMAGE_FILEID', "https://telegra.ph/file/5bb9935be0229adf98b73.jpg")
    MULTI_CLIENT = False
    LOG_CHANNEL = int('-1002107974721')
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str('telegbotnavpan2.onrender.com')
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
    KEEP_ALIVE = str(env.get("KEEP_ALIVE", "0").lower()) in ("1", "true", "t", "yes", "y")


