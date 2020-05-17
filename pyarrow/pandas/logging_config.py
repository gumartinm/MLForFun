import logging


def configure_logging():
    logger = logging.getLogger('pandas')
    logger.setLevel(logging.INFO)
    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
