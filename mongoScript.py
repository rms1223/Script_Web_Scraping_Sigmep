from pymongo import MongoClient
import config
import datetime
class Mongo_Database:

    def __init__(self):
        self.__errorScript = open(config.path_file_error_mongodb,"a")
        self.__errorScript.write(f"Init Mongo Connection {datetime.datetime.now()} \n")

    def mongodb_information_centros_educativos(self):
        try:
            self.client = MongoClient(config.mongo_string_connection)
            self.db =  self.client[config.mongo_database]
            return self.db[config.mongo_collection]
        except Exception as ex:
            self.__errorScript.write(f"MongoDb Error: {ex} {datetime.datetime.now()}\n") 
            
    def close_file(self):
        self.__errorScript.write(f"Finish Mongo Connection {datetime.datetime.now()} \n")
        self.__errorScript.close() 

    