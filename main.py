from project.scheduler.config import init_scheduler
import time
from telegram.ext import ApplicationBuilder
from project.handlers import start
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    scheduler = init_scheduler()
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(start.handler)

    app.run_polling()

if __name__ == '__main__':
    main()