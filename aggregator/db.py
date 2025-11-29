import psycopg2
from contextlib import contextmanager

@contextmanager
def db_conn():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="localhost",
        port="5432"
    )
    try:
        yield conn
    finally:
        conn.close()

def save_rates(date, rates: dict, source: str):
    with db_conn() as conn:
        with conn.cursor() as cur:
            for currency, rate in rates.items():
                cur.execute("""
                    INSERT INTO exchange_rates
                        (date, currency, rate, data_source)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (date, currency, data_source)
                    DO UPDATE SET rate = EXCLUDED.rate;
                """, (date, currency, rate, source))
            conn.commit()
