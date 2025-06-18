import os
import sys

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
    print("- APP_ENV:", Config.APP_ENV)
    print("- DEBUG:", Config.DEBUG)
    print("- SECRET_KEY:", Config.SECRET_KEY)
    print("- DB_HOST:", Config.DB_HOST)
    print("- DB_PORT:", Config.DB_PORT)
    print("- DB_USER:", Config.DB_USER)
    print("- DB_PASSWORD:", Config.DB_PASSWORD)
    

if __name__ == "__main__":
    run()
