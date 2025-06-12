import re
import spacy
from project.news.newsService import NewsService
from project.news.keywordService import KeywordService
from project.news.new import KeyWord
from project.apis.newsDataApi import getNews
from collections import Counter
from datetime import datetime

# Cargar modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

def clean_text(text):
    # Deja solo letras, números y espacios, quita signos de puntuación y símbolos
    text = re.sub(r"[^a-zA-Záéíóúñü0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def extract_keywords(text):
    doc = nlp(text)
    phrases = []
    for chunk in doc.noun_chunks:
        # Lemmatizar token a token y filtrar stopwords
        lemma_phrase = " ".join([token.lemma_ for token in chunk if not token.is_stop])
        lemma_phrase = clean_text(lemma_phrase)

        # Filtro de longitud: descartamos frases muy cortas o muy largas
        if lemma_phrase and len(lemma_phrase) > 2 and len(lemma_phrase.split()) <= 4:
            phrases.append(lemma_phrase)
    return phrases

def save_last_news():
    print("---------- saving -----------")
    newsService = NewsService()
    keywordService = KeywordService()
    news = getNews()

    for n in news:
        newsService.save(n)
        phrases = extract_keywords(n.title)

        # Opcional: podés contar frecuencia acá si querés usarla después
        freq = Counter(phrases)

        for phrase in freq:
            word = KeyWord(phrase, datetime.now())
            keywordService.save(word)