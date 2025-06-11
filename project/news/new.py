from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from project.shared.database import Base


class New(Base):
    __tablename__ = 'news'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    link = Column(String)
    description = Column(String)
    time = Column(String)
    image_url = Column(String)


    def __init__(self, title, link):
        self.title = title
        self.link = link


    
