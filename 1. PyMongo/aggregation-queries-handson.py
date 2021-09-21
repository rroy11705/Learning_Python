import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    try:
        my_client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

        print(my_client)

        my_db = my_client['test']
        collection = my_db['agg_example']

        profiles = [
            {"user": "ram", "title": "Python"},
            {"user": "raj", "title": "Javascript"},
            {"user": "ram", "title": "C++"},
            {"user": "john", "title": "MongoDB"},
            {"user": "rohan", "title": "Perl"},
        ]

        # collection.insert_many(profiles)

        agg_result = collection.aggregate(
            [
                {
                    "$group": {
                        "_id": "$title",
                        "occurrences": {"$sum": 1}
                    }
                }
            ]

        )
        for i in agg_result:
            print(i)

    except ConnectionFailure as e:
        print("Error:", e)


if __name__ == '__main__':
    main()