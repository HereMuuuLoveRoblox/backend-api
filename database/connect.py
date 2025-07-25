import sqlite3
import os
import sys

def ConnectDB():
    try:
        db_path = os.getenv("DB_PATH", "my_database.db")  # ใช้ default ถ้า .env ไม่มี
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        return connection

    except sqlite3.Error as err:
        print(f"Connect DB failed: {err}")
        sys.exit(1)

# Test
if __name__ == "__main__":
    conn = ConnectDB()
    if conn :
        print("Connect Database Success!")
    conn.close()
