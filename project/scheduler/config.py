from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from project.scheduler.tasks import save_last_news
from datetime import datetime, timezone
import logging

scheduler = BackgroundScheduler()
logging.basicConfig(level=logging.INFO)

def init_scheduler():
    logging.info("iniciando scheduler")
    scheduler.add_job(update_job, IntervalTrigger(minutes=70))
    update_job()
    scheduler.start()
    save_last_news()
    
    
def update_job():
    now = datetime.now()
    hour = now.hour - 3

    if 0 <= hour < 6:
        minutes = 60
    elif 6 <= hour < 12:
        minutes = 4
    elif 12 <= hour < 18:
        minutes = 6
    else:
        minutes = 9

    try:
        scheduler.remove_job("save_last_news")
    except:
        pass

    scheduler.add_job(
        save_last_news,
        IntervalTrigger(minutes=minutes),
        id="save_last_news",
        name="save last news"
    )
    logging.info("tasa de refresco actualizada a cada " + str(minutes) + " minutos" )
    