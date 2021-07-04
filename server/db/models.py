from json import JSONEncoder

from sqlalchemy import Column, Integer, String, DateTime, Text, JSON

from server.db import Base


class Article(Base, JSONEncoder):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, index=True)
    modified = Column(DateTime)
    title = Column(Text)
    content = Column(Text)
    author_id = Column(Integer, index=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):

    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(Text)
    avatar = Column(String)
    position = Column(String)
    links = Column(JSON)
    twitter = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
