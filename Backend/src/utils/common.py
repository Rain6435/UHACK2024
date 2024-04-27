import logging

DEBUG_LVL = 12

def get_logger():
    new_logger = logging.getLogger()

    new_logger.setLevel(logging.INFO)

    return new_logger