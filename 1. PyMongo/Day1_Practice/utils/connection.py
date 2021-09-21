from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def make_connection():
    try:
        my_client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
        return my_client

    except ConnectionFailure as e:
        print("Connection Error:", e)