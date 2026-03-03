# config.py
import os
import mysql.connector

# قراءة معلومات MySQL من Environment Variables
DB_HOST = os.getenv("mysql.railway.internal")                  # المضيف
DB_USER = os.getenv("root")                  # اسم المستخدم
DB_PASSWORD = os.getenv("qhMPPqklAOWdIJIrJTMrkIsrywwAmuOe")    # كلمة المرور
DB_NAME = os.getenv("railway")             # اسم قاعدة البيانات
DB_PORT = int(os.getenv("root", 3306))       # المنفذ، الافتراضي 3306

# توكن البوت ورابط المشروع (DOMAIN)
TOKEN = os.getenv("8446018051:AAGOFSu5hsIAyUoVlXnooX3iFGOK4jeOrqI")                        # ضع توكن البوت كـ Variable على Railway
DOMAIN = os.getenv("https://my-bot.up.railway.app")                      # رابط مشروعك على Railway

# إنشاء اتصال قاعدة البيانات
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)
