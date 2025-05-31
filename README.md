# Shivaay Telegram Bot 🤖

A powerful Telegram bot built with **Pyrogram**, ready to deploy easily on **Heroku**.

---

## Features

- Built using Pyrogram (Python Telegram API framework)
- Supports channel and group management
- Sudo users & owner privileges
- Easy configuration via environment variables
- Supports media handling with FFmpeg buildpack on Heroku

---

## 🚀 Deploy to Heroku

You can deploy this bot with just one click to Heroku!

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Shivaay20005/Cobra-exx-main)

---

## Setup & Configuration

1. Fork or clone this repository.

2. Set up environment variables on Heroku (or locally):

| Variable     | Description                                               | Required |
|--------------|-----------------------------------------------------------|----------|
| `API_ID`     | Telegram API ID from https://my.telegram.org               | Yes      |
| `API_HASH`   | Telegram API Hash from https://my.telegram.org             | Yes      |
| `BOT_TOKEN`  | Telegram bot token from [@BotFather](https://t.me/BotFather) | Yes      |
| `BOT_USERNAME` | Your bot's username (without @)                          | Yes      |
| `OWNER_ID`   | Your Telegram User ID (bot owner/admin)                    | Yes      |
| `SUDO_USERS` | Comma-separated list of additional sudo user IDs (optional) | No       |
| `CHANNEL_ID` | Telegram channel ID (usually starts with -100)             | Yes      |

3. Add a `Procfile` with the content:

