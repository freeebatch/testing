# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27881923"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "79abda5e46a51fc0dce1313f2548ce19")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6000596785:AAEkl4KxA9Nbooh-Qezy6Z3r0XFKarg1lfA")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Txtdownloaderbyanu_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1671836568"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002370656932"))
# ------------------------------------------------
# MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# # -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002370656932"))

