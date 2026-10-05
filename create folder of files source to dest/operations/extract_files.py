from utils import logger
import os
logger = logger.get_logger(__name__)

def fetch_files(source_path):
    try:
        files_list = [file for file in os.listdir(source_path)]
        logger.info(f'fetch files from {source_path}')
        return files_list
    except Exception as e:
        logger.error(f'fetch files from {e} failed')
