from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25449636"))
API_HASH = getenv("API_HASH", "b502058c5b53c90017d363b69f87e492)
BOT_TOKEN = getenv("BOT_TOKEN", "5670167712:AAEFiapr2olvWRF4Uhxo9hxa14f93gY_Y30")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu4h0syFGasDSwz2YP8G86LvJwCIzcDUTRwIaTi51W8YUl4oiMMbiqQ-98i2X_6Yiic2GxxkA31jZWjNHGBI7meVQvEIQMOETP7ZiPE1f4r0kwTmKjJp7fvezUWJbMhUKuRm5OQ7CIK9SaJAD1RA1DFvBvIulFDnuud9oAmMkAF-IpLf1PstFZPzM-wyiuNw-E92opkpqMiuEY4qS9rpnIT6G_I9SUAvxGh78W7k_qhZY3QvkIiII0unAgfcjGzxFMzU20asOlBmWA4YnWT4y8dtvEtSzKfei4p-j50DGnUF3UNW5ATscKlE0acCroxoDJy8HrLfh1J5mhae43QpR3Mo=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "L1_Y2")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Fix1izbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "iiii_o13")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6085572557").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6085572557").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
