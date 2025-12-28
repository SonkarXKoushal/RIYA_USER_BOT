import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27079591")) #optional
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7668520999").split()))
OWNER_ID = int(getenv("OWNER_ID", 8009369344))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7907566055:AAFXzaaqXYBraXLs50OhFyMqN8g9BK8zW4c")
ALIVE_PIC = getenv("ALIVE_PIC", "https://files.catbox.moe/2731lh.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/SonkarXKoushal/RIYA_USER_BOT")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "ATUAAv4AAQEAATSwc3GI-tW6F0ztIQSuc6PMbrtlpuw1DDoJsT4zAmCjzgpz_jH14uJK_x08GG4nqsgFIlCkKORp7II4iulEWWsJVWiicBvf4VLmdN0Ytv5Xr9Rz6uXTwz9dndGkGfIs3hbLEFjq04d_2Uw2_jrzymfEK-KrCGr5fg4g_3czLmtPXTDIlr6EcPKhdNcsEk4Jlflph3x-6l9XrvQBifkRGk4UEpSGPxmKd-GuugWD_Mbu2doXeCEPacAeCh4YgUjFl8g-bC_MPGoyKVuUNcwSfGjhSW-i7bpJWuMrWqtJRYyVQ-617fnKqYCIuIke-CLRqcudJkIrK-cGsOif9EDlzh8F8JEBAAExo308AQAD")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
