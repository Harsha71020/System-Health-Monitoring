
import psutil
import sqlite3
import time
from datetime import datetime

def log_metrics():
    conn = sqlite3.connect("system_metrics.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS metrics
                      (timestamp TEXT, cpu REAL, memory REAL, disk REAL)''')

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)", (timestamp, cpu, memory, disk))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    while True:
        log_metrics()
        print("Logged system metrics.")
        time.sleep(60)  # Log every 60 seconds
