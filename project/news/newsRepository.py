from project.shared.database import get_session
from project.news.new import New
from sqlalchemy import desc


class NewsRepository:
    def __init__(self):
        self.session = get_session()

    def save(self, new: New):
        self.session.add(new)
        self.session.commit()

    def getAll(self):
        return self.session.query(New).all()

    def getById(self, id):
        return self.session.query(New).filter(New.id == id).first()

    def refresh(self, new: New):
        # Por simplicidad, asumiendo new ya está enlazada a sesión
        self.session.commit()

    def remove(self, new: New):
        self.session.delete(new)
        self.session.commit()

    def getLast(self, amount):
        return self.session.query(New).order_by(desc(New.time)).limit(amount).all()
