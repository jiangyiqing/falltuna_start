import logging


def get_logger():
    fastapi_logger = logging.getLogger()
    fh = logging.FileHandler("main_log.log")
    fh.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    fastapi_logger.addHandler(fh)
    return fastapi_logger
