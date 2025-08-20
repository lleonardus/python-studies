import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()
DATABASE_URL = os.getenv(key="DATABASE_URL", default="sqlite:///database.db")

engine = create_engine(url=DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
