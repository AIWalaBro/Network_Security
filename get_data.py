import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
load_dotenv()

# Collection MongoDB URL
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ce = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise  NetworkSecurityException(e, sys)
        

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # convert csv data into json format
            records = list((json.loads(data.T.to_json())).values())
            return records
            
        except Exception as e:
            raise  NetworkSecurityException(e, sys)
            
        
    def pushing_data_to_mongodb(self, records, database, collection):
        try:
            self.records    = records
            self.database   = database
            self.collection = collection

            # for pushing record intialise the client through pymongo
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database     = self.mongo_client[self.database]
            self.collection   = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)


        except Exception as e:
            raise  NetworkSecurityException(e,sys)


if __name__ == "__main__":
    FILE_PATH  = "./Network_Data/NetworkData.csv"
    DATABASE   = "AIWalaBro_Database"
    COLLECTION = "Network_Security_Collection"

    # you have to create object of the class and call the function
    network_obj = NetworkDataExtract()
    network_json_records = network_obj.csv_to_json_converter(FILE_PATH)
    mongodb_pusher = network_obj.pushing_data_to_mongodb(network_json_records, DATABASE, COLLECTION)
    print(mongodb_pusher)
