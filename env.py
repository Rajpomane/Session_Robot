import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "10606993").strip()
API_HASH = os.getenv("API_HASH", "c04a8a54e450831f8868b17366291058").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6077261060:AAHhc0XjNBFRqDh_C4J-D_ojwP2HOioShRo").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/LOVERS_POINTT")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
