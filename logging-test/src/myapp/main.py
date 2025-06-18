import os
import sys

import xml.etree.ElementTree as ET
import re
import logging
from collections import defaultdict
from config.base_config import Config

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def method01():
    logger.info('method01 begin')
    logger.info('method01 end')
    return 'ok'

def method02():
    logger.info('method02 begin')
    logger.info('method02 end')
    return 'ok'

def run():
    logger.info("- APP_ENV:", Config.APP_ENV)
    logger.info("- DEBUG:", Config.DEBUG)
    logger.info("- SECRET_KEY:", Config.SECRET_KEY)
    logger.info("- DB_HOST:", Config.DB_HOST)
    logger.info("- DB_PORT:", Config.DB_PORT)
    logger.info("- DB_USER:", Config.DB_USER)
    logger.info("- DB_PASSWORD:", Config.DB_PASSWORD)
    

if __name__ == "__main__":
    run()
