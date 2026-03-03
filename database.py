import mysql.connector
from mysql.connector import pooling
from config import DB_CONFIG

class Database:
    def __init__(self):
        self.pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            **DB_CONFIG
        )

    def get_conn(self):
        return self.pool.get_connection()

    def get_user(self, user_id):
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    def create_withdrawal(self, user_id, amount, wallet):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO withdrawals (user_id, amount, wallet_address) VALUES (%s,%s,%s)",
            (user_id, amount, wallet),
        )
        conn.commit()
        cursor.close()
        conn.close()

    def has_pending_withdrawal(self, user_id):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM withdrawals WHERE user_id=%s AND status='pending' LIMIT 1",
            (user_id,),
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
