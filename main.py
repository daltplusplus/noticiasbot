from project.scheduler.config import init_scheduler
import time
from telegram.ext import ApplicationBuilder
from project.handlers import start
from dotenv import load_dotenv
import os
from telegram.request import HTTPXRequest

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

request = HTTPXRequest(
    connect_timeout=30.0,  
    read_timeout=30.0,     
    write_timeout=30.0,    
    pool_timeout=30.0      
)

def main():
    scheduler = init_scheduler()
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()

    app.add_handler(start.handlerNow)
    app.add_handler(start.handlerStart)
    app.add_handler(start.handlerTop)

    app.run_polling()

if __name__ == '__main__':
    main()