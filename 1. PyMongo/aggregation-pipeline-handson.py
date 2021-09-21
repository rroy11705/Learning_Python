import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.son import SON
import pprint


def main():
    try:
        my_client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

        print(my_client)

        my_db = my_client['test']
        collection = my_db['agg_pipeline_example']

        sample_data = [
            {"x": 1, "tags": ["dog", "cat"]},
            {"x": 2, "tags": ["cat"]},
            {"x": 2, "tags": ["mouse", "dog", "cat"]},
            {"x": 3, "tags": []},
        ]

        collection.insert_many(sample_data)

        pipeline = [
                {"$unwind": "$tags"},    # make a flat hierarchy
                {
                    "$group": {                     # actual aggregation
                        "_id": "$tags",
                        "count": {"$sum": 1}
                    }
                },
                {
                    "$sort": SON([("count", -1), ("_id", -1)])           # sort
                }
            ]

        pprint.pprint((list(collection.aggregate(pipeline))))

    except ConnectionFailure as e:
        print("Error:", e)


if __name__ == '__main__':
    main()
