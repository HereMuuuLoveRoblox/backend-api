import sqlite3
import os
import sys

def TestConnectDB():
    try:
        db_path = os.getenv("DB_PATH", "my_database.db")  # ใช้ default ถ้า .env ไม่มี
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        return connection

    except sqlite3.Error as err:
        print(f"Connect DB failed: {err}")
        sys.exit(1)

def get_db():
    db_path = os.getenv("DB_PATH", "my_database.db")
    connection = sqlite3.connect(db_path, check_same_thread=False)  # ✅ เหมือนกัน
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()
        
# Test
if __name__ == "__main__":
    conn = TestConnectDB()
    if conn :
        print("Connect Database Success!")
    conn.close()
