from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .collectors.api_collector import APICollector
from .parsers.api_parser import APIParser
from .db import save_rates

API_SOURCES = [
    {"name": "ECB", "endpoint": "https://api.exchangerate.host/latest"}
]

def collect_all():
    print("Сбор данных начат ->", datetime.now())
    for source in API_SOURCES:
        collector = APICollector(source["endpoint"])
        data = collector.fetch()
        rates = APIParser.parse(data)
        save_rates(datetime.now().date(), rates, source["name"])
        print("Данные из", source["name"], "сохранены.")
    print("Сбор данных завершён.")

def launch_scheduler(interval_minutes=60):
    scheduler = BackgroundScheduler()
    scheduler.add_job(collect_all, "interval", minutes=interval_minutes, next_run_time=datetime.now())
    scheduler.start()
