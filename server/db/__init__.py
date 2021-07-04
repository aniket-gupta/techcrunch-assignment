from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config

db = create_engine(Config.DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(db)


def create_tables():
    Base.metadata.drop_all(db)
    Base.metadata.create_all(db)
