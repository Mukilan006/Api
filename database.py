import pymysql
from settings import Settings

settings = Settings()


def get_connection():
    return pymysql.connect(
        host=settings.DATABASE["host"],
        user=settings.DATABASE["user"],
        password=settings.DATABASE["password"],
        db=settings.DATABASE["database"],
        port=settings.DATABASE["port"],
        cursorclass=pymysql.cursors.Cursor,
        autocommit=True,  # Optional: use if you don’t want to call commit() manually
    )
