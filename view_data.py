import sqlite3

def view_metrics():
    try:
        conn = sqlite3.connect("system_metrics.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC")
        rows = cursor.fetchall()

        if rows:
            print(f"{'Timestamp':<20} {'CPU (%)':<10} {'Memory (%)':<12} {'Disk (%)':<10}")
            print("-" * 60)
            for row in rows:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<12} {row[3]:<10}")
        else:
            print("No data found in the database.")

        conn.close()

    except Exception as e:
        print("Error reading database:", e)

if __name__ == "__main__":
    view_metrics()
