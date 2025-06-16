from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from project.news.newsService import NewsService
from project.news.keywordService import KeywordService
import logging
from datetime import date, datetime
import pytz

logging.basicConfig(level=logging.INFO)
timezone_ar = pytz.timezone("America/Argentina/Buenos_Aires")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Hola! soy canillita. Puedo ayudarte a ver las noticias y tendencias del dia\n"
    message += "\nPodes controlarme con los estos comandos:\n"
    message += "\n/ultimo - las ultimas noticias"
    message += "\n/top - temas mas mencionados hoy hasta ahora"
    message += "\n/buscar [palabra] - ultimas noticias que contenga dicha palabra"

    await update.message.reply_text(message, parse_mode='HTML')

async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("enviando ultimas noticias")
    newsService = NewsService()
    news = newsService.getLast(3)

    message = "<b>📢 Últimas noticias:</b>\n\n"
    for n in news:
        dif = datetime.now(timezone_ar).replace(tzinfo=None) - n.time.replace(tzinfo=None) 
        message += f"📰 <a href=\"{n.link}\">{n.title}</a>\n"
        if dif.total_seconds() / 60 > 120:
            hours = round(dif.total_seconds() / 3600)
            message += f"Fuente: {n.source_name} | hace {hours} horas\n\n"
        else:
            minutes = round(dif.total_seconds() / 60)
            message += f"Fuente: {n.source_name} | hace {minutes} minutos\n\n"
        
    await update.message.reply_text(message, parse_mode='HTML')

async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("mostrando top")
    keywordService = KeywordService()
    today = datetime.now(timezone_ar).date()
    words = keywordService.getDateTop(dateToSearch=today)
    top = words[:7]
    message = "<b>🔥 Temas más mencionados hoy:</b>\n"
    for wd, ts in top:
        message += f"🔹{wd} ({ts} menciones)\n"
        
    await update.message.reply_text(message, parse_mode='HTML')

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    searchedWord = context.args[0]
    logging.info("buscando resultados con palabra " + searchedWord)
    newsService = NewsService()
    news = newsService.getByWord(searchedWord)

    message = "<b>📚 noticias que contengan '" + searchedWord + "':</b>\n\n"
    for n in news:
        dif = datetime.now(timezone_ar).replace(tzinfo=None) - n.time.replace(tzinfo=None) 
        message += f"📰 <a href=\"{n.link}\">{n.title}</a>\n"
        if dif.total_seconds() / 60 > 120:
            hours = round(dif.total_seconds() / 3600)
            message += f"Fuente: {n.source_name} | hace {hours} horas\n\n"
        else:
            minutes = round(dif.total_seconds() / 60)
            message += f"Fuente: {n.source_name} | hace {minutes} minutos\n\n"
        
    await update.message.reply_text(message, parse_mode='HTML')

    

def escape_markdown_v2(text: str) -> str:
    escape_chars = r'_[]()~`>#+-=|{}.!'
    return ''.join('\\' + c if c in escape_chars else c for c in text)

handlerNow = CommandHandler("ultimo", now)
handlerStart = CommandHandler("start", start)
handlerTop = CommandHandler("top", top)
handlerSearch = CommandHandler("buscar", search)