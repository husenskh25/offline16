#1.create source folder having csv,pdf,json,yaml files 
#dump into destination directory -- csv file should be into csv dir
#pdf file into pdf dir etc..


#-use :professional code practice [functions,modules,packages]
#-use exception handling
#-use -  logger 



from utils import logger
import os
from operations import extract_files as e
from operations import read_data as r
from operations import write_file as w
from operations import pdf_reader as p
from operations import pdf_writer as wp





logger = logger.get_logger(__name__)







def main():
    logger.info(f'start {__name__}')

    source_path = r'D:\source'
    dest_path = r'D:\destination'


    file_list = e.fetch_files(source_path)


    logger.info(f'fetch files from {source_path} successfully')

    for file in file_list:

        if file.endswith('.csv'):

            folder = 'csv'

            data = r.read_file(file, source_path)

            folder_path = os.path.join(dest_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                w.write_file(data, file, dest_path, folder)
            else:
                w.write_file(data, file, dest_path, folder)

        elif file.endswith('.txt'):
            folder = 'txt'
            data= r.read_file(file, source_path)
            folder_path = os.path.join(dest_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                w.write_file(data, file, dest_path, folder)
            else:
                w.write_file(data, file, dest_path, folder)

        elif file.endswith('.json'):
            folder = 'json'
            data= r.read_file(file, source_path)
            folder_path = os.path.join(dest_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                w.write_file(data, file, dest_path, folder)
            else:
                w.write_file(data, file, dest_path, folder)

        elif file.endswith('.yaml')or file.endswith('.yml'):
            folder = 'yaml'
            data= r.read_file(file, source_path)
            folder_path = os.path.join(dest_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                w.write_file(data, file, dest_path, folder)
            else:
                w.write_file(data, file, dest_path, folder)
        elif file.endswith('.pdf'):
            folder = 'pdf'
            data = p.pdf_reader(file, source_path)
            folder_path = os.path.join(dest_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                wp.pdf_writer(folder, file, dest_path, data)
            else:
                wp.pdf_writer(folder, file, dest_path, data)



if __name__ == '__main__':
    main()