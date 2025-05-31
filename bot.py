import os
import sys
import time
from pyrogram import Client
from pyrogram.errors import FloodWait

# Fetch credentials from Heroku config vars (Environment Variables)
API_ID = int(os.getenv("API_ID", "0"))           # Your Telegram API ID (integer)
API_HASH = os.getenv("API_HASH", "")              # Your Telegram API Hash (string)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")            # Your Bot Token (string)

if not API_ID or not API_HASH or not BOT_TOKEN:
    print("ERROR: Missing one or more environment variables: API_ID, API_HASH, BOT_TOKEN")
    sys.exit(1)

# Initialize Pyrogram Client with session name (can be any string)
app = Client(
    session_name="my_bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def start_bot():
    try:
        print("[INFO] Starting bot...")
        app.start()
        print("[INFO] Bot started successfully!")
        app.idle()  # Keep the bot running until interrupted
    except FloodWait as e:
        print(f"[WARNING] FloodWait error! Need to wait {e.x} seconds before retrying...")
        time.sleep(e.x)
        print("[INFO] Retrying to start bot now...")
        start_bot()  # Recursive retry after waiting
    except Exception as e:
        print(f"[ERROR] Unexpected error occurred: {e}")
        print("[INFO] Exiting with status 1 to allow Heroku to restart the dyno if needed.")
        sys.exit(1)

if __name__ == "__main__":
    start_bot()
