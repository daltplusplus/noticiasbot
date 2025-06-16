import requests
from project.news.new import New
from datetime import datetime
import pytz

no_appendable= ["/colombia/", "/mexico/", "/espana/", ".es", "/peru/"]
timezone_ar = pytz.timezone("America/Argentina/Buenos_Aires")

def getNews():
    # Llamar a una API que devuelve una imagen por URL
    response = requests.get("https://newsdata.io/api/1/latest?apikey=pub_071d8251a71e44e495ae9c38ab439c58&country=ar&language=es")
    if response.status_code == 200:
        data = response.json()
        news = []
        for article in data["results"]:
            link = article["link"]
            if not cant_append(link):
                title = article["title"]
                
                new = New(title, link)
                
                new.source_name = article["source_name"]
                new.image_url = article["image_url"]
                new.description = article["description"]
                new.time = datetime.now(timezone_ar)

                news.append(new)
                
                

    return news


def cant_append(link):
    counts = 0
    for n in no_appendable:
        counts += link.count(n)
    
    return counts
        
