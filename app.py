import logging
import os

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import file_handler, pdf_converter

# Replace with your bot token, API ID, and API Hash
BOT_TOKEN = '7220840802:AAEYee75LzRu9Y6gtECw6buuh3Azy_ZSJ7c'
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update: Update, context):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_html(
        rf"Hi {user.mention_html()}! Send me a CBZ file to convert to PDF."
    )

def convert_cbz_to_pdf(update: Update, context):
    """Handles the CBZ file conversion."""
    user = update.message.from_user
    file_id = update.message.document.file_id

    try:
        file_path = file_handler.download_file(context.bot, file_id)
        pdf_path = pdf_converter.convert_cbz_to_pdf(file_path)
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(pdf_path, 'rb'))
        file_handler.delete_files(file_path, pdf_path)
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    """Start the bot."""
    bot = Bot(token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
    updater = Updater(bot=bot, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, convert_cbz_to_pdf))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
