import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AUTHORIZED_USERS = [int(uid.strip()) for uid in os.getenv("AUTHORIZED_USERS", "").split(",") if uid.strip().isdigit()]
