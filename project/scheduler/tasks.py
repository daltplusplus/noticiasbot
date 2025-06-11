from project.news.newsRepository import NewsRepository
from project.apis.newsDataApi import getNews

def save_last_news():
    print("----------saving-----------")
    repo = NewsRepository()
    news = getNews()
    for n in news:
        repo.save(n)