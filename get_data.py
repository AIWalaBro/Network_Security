import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

# Collection MongoDB URL
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ce = certifi.where()

import pandas as pd
import numpy as np
import pymongo


from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.logger.logger import logging




class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise  NetworkSecurityException(e, sys)
        

    def csv_to_json_converter(self):
        try:
            pass
        except Exception as e:
            raise  NetworkSecurityException(e, sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise  NetworkSecurityException(e,sys)

if __name__ == "__main__":
    pass