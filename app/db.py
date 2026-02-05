import os 
import pymysql
from sqlalchemy import create_engine

#Doceker db connection
def get_engine():
    user = os.getenv("DB_USER", "analyst")
    pw = os.getenv("DB_PASS", "analyst")
    host = os.getenv("DB_HOST","127.0.0.1")
    port = os.getenv("DB_PORT","33306")
    db = os.getenv("DB_NAME","national_parks")
    return create_engine(f"mysql+pymysql://{user}:{pw}@{host}:{port}/{db}")