from utils import logger
import os
logger= logger.get_logger(__name__)


def write_file(data, file_name, dest_path, folder):
    try:

        filename = os.path.join(dest_path, folder, file_name)

        with open(filename, 'w') as fp:
            fp.write(data)

        logger.info(f'write file {file_name} to {dest_path}')

    except Exception as e:
        logger.error(f'write file {file_name} failed')