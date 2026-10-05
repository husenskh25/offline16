from utils import logger
import os


logger = logger.get_logger(__name__)


def read_file(file_name, source_path):
    try:
        with open(os.path.join(source_path, file_name), 'r') as fp:
            data = fp.read()

        logger.info(f'read file {file_name} from {source_path}')
        return data
    except Exception as e:
        logger.error(f'read file {file_name} failed')