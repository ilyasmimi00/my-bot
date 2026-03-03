# config.py
import os
from pymongo import MongoClient

# قراءة المتغيرات من Environment Variables
MONGODB_URI = os.getenv("mongodb+srv://eliasguerbas_db_user:baydonN1992@cluster0.gxisjmy.mongodb.net/botdb?retryWrites=true&w=majority")
TOKEN = os.getenv("8446018051:AAGOFSu5hsIAyUoVlXnooX3iFGOK4jeOrqI")
DOMAIN = os.getenv("https://my-bot.up.railway.app")

# تحقق أن القيم موجودة
if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set in environment variables")

if not TOKEN:
    raise ValueError("TOKEN is not set in environment variables")

if not DOMAIN:
    raise ValueError("DOMAIN is not set in environment variables")

# إنشاء الاتصال بقاعدة البيانات
client = MongoClient(MONGODB_URI)

# اختيار قاعدة البيانات
db = client["botdb"]

print("✅ MongoDB connected successfully")