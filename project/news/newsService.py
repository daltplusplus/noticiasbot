from project.news.newsRepository import NewsRepository
from project.news.new import New



class NewsService:
    def __init__(self):
        self.repo = NewsRepository()

    def save(self, new: New):
        self.repo.save(new)

    def getAll(self):
        return self.repo.getAll

    def getById(self, id):
        return self.repo.getById(id)

    def refresh(self, new: New):
        self.repo.refresh()

    def remove(self, new: New):
        self.repo.remove(new)

    def getLast(self, amount):
        return self.repo.getLast(amount)