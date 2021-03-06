import os

from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv(verbose=True, dotenv_path='secrets.env')

# Clients DB names
SANTANDER_DB_NAME = 'santander'
USERS_DB_NAME = 'users'
RCMS_DB_NAME = 'rcms'


class DBHandler:

    def __init__(self):
        self.__db_user = os.getenv("DB_USER")
        self.__db_password = os.getenv("DB_PASSWORD")
        self.__db_url = f'mongodb+srv://{self.__db_user}:{self.__db_password}@cluster0-mx9ah.mongodb.net/test?retryWrites=true&w=majority'
        self.__client = MongoClient(self.__db_url)

    def get_client_db(self, client_name):
        return self.__client[client_name]

    def close(self):
        if self.__client is not None:
            self.__client.close()

    def __del__(self):
        self.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __enter__(self):
        return self
