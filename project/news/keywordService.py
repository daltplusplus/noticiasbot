from project.news.keywordRepository import KeywordRepository
from project.news.new import KeyWord
from collections import Counter



class KeywordService:
    def __init__(self):
        self.repo = KeywordRepository()

    def save(self, word: KeyWord):
        self.repo.save(word)

    def getDateTop(self, dateToSearch):
        keywords = self.repo.getAllByDate(dateToSearch)
        words = [kw.word for kw in keywords]

        counter = Counter(words)

        lista_ordenada = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return lista_ordenada

