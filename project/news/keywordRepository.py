from project.shared.database import get_session
from project.news.new import KeyWord
from sqlalchemy import desc, func
from datetime import date


class KeywordRepository:
    def __init__(self):
        self.session = get_session()

    def save(self, word: KeyWord):
        self.session.add(word)
        self.session.commit()

    def getAllByDate(self, dateToSearch):
        return self.session.query(KeyWord).filter(
            func.date(KeyWord.date) == dateToSearch).all()