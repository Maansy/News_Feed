from dotenv import load_dotenv
import os
from flask_restx import Api

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', 'mansy123'),
    'db': os.getenv('DB_NAME', 'news_feeds')
}