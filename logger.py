import logging
import logging.config
import os

logger = logging.getLogger('dev')
with open("/Users/sid/next-company-prep/ottomason/logging.ini", "r") as config_file:
    logging.config.fileConfig(config_file)
