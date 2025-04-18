import logging

def get_logger(name="db_tool"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )
        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger