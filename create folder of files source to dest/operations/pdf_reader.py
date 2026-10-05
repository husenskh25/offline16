from utils import logger
import os
from pypdf import PdfReader

logger = logger.get_logger(__name__)
def pdf_reader(file_name, source_path):
    try:
        pdf_path = os.path.join(source_path, file_name)

        reader = PdfReader(pdf_path)

        data = ''

        for page in reader.pages:
            data += page.extract_text() or ''

        logger.info(f'read pdf file {file_name}')

        return data

    except Exception as e:
        logger.error(f'read pdf file {file_name} failed: {e}')
        return None

