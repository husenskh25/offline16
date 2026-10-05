from utils import logger
import os
from reportlab.pdfgen import canvas

logger = logger.get_logger(__name__)


def pdf_writer(folder, file_name, dest_path, data):


    try:
        pdf_path = os.path.join(dest_path, folder, file_name)

        c = canvas.Canvas(pdf_path)

        c.drawString(50, 750, data)

        c.save()

        logger.info(f'write pdf file {file_name} to {dest_path}')



    except Exception as e:
        logger.error(f'write pdf file {file_name} failed: {e}')
