from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from project.news.newsRepository import NewsRepository


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Puedo mostrarte las noticias del dia en Argentina\n"
    message += "\nPodes controlarme con los estos comandos:\n"
    message += "\n/now - las ultimas noticias de hoy"

async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    repo = NewsRepository()
    news = repo.getLast(3)

    for n in news:
        message = ""
        message += "*" + n.title + "*\n"
        message += "\n"
        if not n.description is None:
            message += n.description + "\n"
            message += "\n"
        message += n.link
        message += "\n"
        message += "\n"
        scaped_message = escape_markdown_v2(message)
        await update.message.reply_text(scaped_message, parse_mode="MarkdownV2")
    
    

def escape_markdown_v2(text: str) -> str:
    escape_chars = r'_[]()~`>#+-=|{}.!'
    return ''.join('\\' + c if c in escape_chars else c for c in text)

handler = CommandHandler("now", now)