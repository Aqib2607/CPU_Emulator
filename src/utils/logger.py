# src/utils/logger.py

import logging

# Set up logger
logging.basicConfig(level=logging.INFO)

def log(message):
    logging.info(message)
