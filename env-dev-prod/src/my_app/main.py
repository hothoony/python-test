import os
import sys

# Add the project root directory to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import xml.etree.ElementTree as ET
import re
from collections import defaultdict
from config.base_config import Config

def method01():
    print('method01 begin')
    print('method01 end')
    return 'ok'

def method02():
    print('method02 begin')
    print('method02 end')
    return 'ok'

def run():
    print("환경:", Config.APP_ENV)
    print("디버그 모드:", Config.DEBUG)
    print("DB 호스트:", Config.DB_HOST)
    print("DB 포트:", Config.DB_PORT)
    print("시크릿 키:", Config.SECRET_KEY)

if __name__ == "__main__":
    run()
