import time
import psycopg2
import os

db_host = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT")
db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USERNAME")
db_pass = os.getenv("DATABASE_PASSWORD")

while True:
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port
        )
        conn.close()
        print("Database is ready!")
        break
    except psycopg2.OperationalError:
        print("Database not ready yet, waiting...")
        time.sleep(2)
