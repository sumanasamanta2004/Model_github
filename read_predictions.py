# read_predictions.py

import sqlite3
import time

def read_new_predictions():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    last_seen_id = 0

    print("🔁 Starting prediction monitor (checks every 90 seconds)...")

    while True:
        cursor.execute("SELECT * FROM predictions WHERE id > ?", (last_seen_id,))
        new_predictions = cursor.fetchall()

        if new_predictions:
            print(f"\n🔔 New predictions at {time.strftime('%H:%M:%S')}:\n")
            for row in new_predictions:
                id, sl, sw, pl, pw, label = row
                print(f"ID {id}: [{sl}, {sw}, {pl}, {pw}] => {label}")
                last_seen_id = max(last_seen_id, id)
        else:
            print(f"⏰ No new predictions at {time.strftime('%H:%M:%S')}")

        time.sleep(90)

if __name__ == "__main__":
    read_new_predictions()
