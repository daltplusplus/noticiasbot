import requests
from project.news.new import New
from datetime import datetime, timezone
from project.news.newsRepository import NewsRepository

def getNews():
    # Llamar a una API que devuelve una imagen por URL
    response = requests.get("https://newsdata.io/api/1/latest?apikey=pub_071d8251a71e44e495ae9c38ab439c58&country=ar&language=es&category=top&timezone=America/Argentina/Buenos_Aires")
    if response.status_code == 200:
        data = response.json()
        news = []
        for article in data["results"]:
            title = article["title"]
            link = article["link"]

            new = New(title, link)

            new.image_url = article["image_url"]
            new.description = article["description"]
            new.time = datetime.now()

            news.append(new)
            print(new.title)

    return news


        
