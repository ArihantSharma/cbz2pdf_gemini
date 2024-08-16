import os
import tempfile

def download_file(bot, file_id):
    """Downloads a file from Telegram."""
    file = bot.get_file(file_id)
    file_path = os.path.join(tempfile.gettempdir(), file.file_path.split('/')[-1])
    file.download(file_path)
    return file_path

def delete_files(*files):
    """Deletes multiple files."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)
