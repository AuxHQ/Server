import os

from dotenv import load_dotenv

from sqlalchemy import URL

load_dotenv()


class Settings:
    PROJECT_NAME = "Aux"

    MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    SQLALCHEMY_DATABASE_URL = URL.create(
        "mysql",
        username=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE
    )

    LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
    LASTFM_API_SECRET = os.getenv("LASTFM_API_SECRET")


settings = Settings()
