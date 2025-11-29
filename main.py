import os
from aggregator.tasks import launch_scheduler, collect_all

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Exchange Rate Aggregator")
    parser.add_argument('--collect-now', action='store_true', help="Запустить сбор вручную")
    parser.add_argument('--interval', type=int, default=int(os.getenv("SCRAPING_INTERVAL_MINUTES", 60)), help="Интервал сбора в минутах")
    args = parser.parse_args()

    if args.collect_now:
        collect_all()
    else:
        launch_scheduler(interval_minutes=args.interval)
        print("Планировщик запущен. Для выхода нажмите Ctrl+C")
        try:
            import time
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            print("\nЗавершение работы.")
