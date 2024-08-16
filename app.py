import logging
import os
import shutil

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import file_handler, pdf_converter

# Replace with your bot token, API ID, and API Hash
BOT_TOKEN = 'YOUR_BOT_TOKEN'
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# ... rest of your code ...
