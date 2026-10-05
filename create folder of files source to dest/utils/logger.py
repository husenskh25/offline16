import logging
def get_logger(Filename):
    logging.basicConfig(filename='logfile.log',level=10,  filemode='w', format='%(asctime)s - %(levelname)s-%(module)s- %(funcName)s %(name)s - %(message)s')

    logger = logging.getLogger(Filename)
    return logger
