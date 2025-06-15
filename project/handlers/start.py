from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from project.news.newsService import NewsService
from project.news.keywordService import KeywordService
import logging
from datetime import date

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Puedo mostrarte las noticias del dia en Argentina\n"
    message += "\nPodes controlarme con los estos comandos:\n"
    message += "\n/now - las ultimas noticias de hoy"

    await update.message.reply_text(message, parse_mode='HTML')

async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("enviando ultimas noticias")
    newsService = NewsService()
    news = newsService.getLast(3)

    message = "<b>📢 Últimas noticias:</b>\n\n"
    for n in news:
        message += f"📰 <a href=\"{n.link}\">{n.title}</a>\n"
        message += f"Fuente: {n.source_name}\n\n"
        
    await update.message.reply_text(message, parse_mode='HTML')

async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("mostrando top")
    keywordService = KeywordService()
    words = keywordService.getDateTop(dateToSearch=date.today())
    top = words[:5]
    message = "<b>🔥 Temas más mencionados hoy:</b>\n"
    for wd, ts in top:
        message += f"•{wd}, {ts} menciones\n"
        
    await update.message.reply_text(message, parse_mode='HTML')
    

def escape_markdown_v2(text: str) -> str:
    escape_chars = r'_[]()~`>#+-=|{}.!'
    return ''.join('\\' + c if c in escape_chars else c for c in text)

handlerNow = CommandHandler("ultimo", now)
handlerStart = CommandHandler("start", start)
handlerTop = CommandHandler("top", top)