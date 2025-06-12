from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from project.shared.database import Base


class New(Base):
    __tablename__ = 'news'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    link = Column(String)
    description = Column(String)
    time = Column(DateTime)
    image_url = Column(String)
    source_name = Column(String)


    def __init__(self, title, link):
        self.title = title
        self.link = link

class KeyWord(Base):
    __tablename__ = 'keywords'

    id = Column(Integer,primary_key=True)
    word = Column(String)
    date = Column(DateTime)

    def __init__(self, word, date):
        self.word = word
        self.date = date
