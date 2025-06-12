from project.news.keywordRepository import KeywordRepository
from project.news.new import KeyWord



class KeywordService:
    def __init__(self):
        self.repo = KeywordRepository()

    def save(self, word: KeyWord):
        self.repo.save(word)