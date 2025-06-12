from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from project.scheduler.tasks import save_last_news

def init_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        save_last_news,
        IntervalTrigger(minutes=8),
        name="save last news"
    )

    scheduler.start()
    print("Scheduler iniciado.")
    save_last_news()
    return scheduler