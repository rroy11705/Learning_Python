import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    try:
        my_client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

        print("connection successful", my_client)

        my_db = my_client['test']
        collection = my_db['teacher']

        try:
            report = collection.find({}).sort('_id', -1)
            print(report[0])

        except IndexError as ie:
            print("IndexError")
            record = {
                "name": "SKD",
                "teaches": ["DBMS", "Java", "C++"],
                "experience": 10
            }
            collection.insert_one(record)

    except ConnectionFailure as e:
        print("error", e)


if __name__ == '__main__':
    main()