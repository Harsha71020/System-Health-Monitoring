from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetch_metrics():
    conn = sqlite3.connect("system_metrics.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 50")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    data = fetch_metrics()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
