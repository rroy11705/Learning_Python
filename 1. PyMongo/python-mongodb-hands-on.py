# install mongodb on local
# check cli by using mongo --host

# 1. Database up and running
# python + mongo ==> pymongo

# 1. connect to mongodb using python

import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    try:
        my_client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

        print("connection successful", my_client)

        # list down the database
        # list_of_db = my_client.list_databases()
        # print("database available in mongodb", list_of_db)
        #
        # # 2. create new database in mongodb
        mydb = my_client['test']
        # print("database created...", mydb)
        #
        # #create collection
        # collection = mydb['student']
        # record = {
        #     "_id": 0,
        #     "name": "Raj",
        #     "roll_number": 101,
        #     "branch": "cse",
        #     "marks": 90
        # }
        # # 3. insert one record
        # record1 = collection.insert_one(record)
        # print("records", record1),
        #
        # list_of_db = my_client.list_databases()
        # print("database available in mongodb after creation", list_of_db)

        my_list = [
                    {
                        "_id": 10,
                        "name": "John",
                        "roll_number": 102,
                        "branch": "cse",
                        "marks": 90
                    },
                    {
                        "_id": 11,
                        "name": "Rahul",
                        "roll_number": 103,
                        "branch": "cse",
                        "marks": 89
                    },
                    {
                        "_id": 12,
                        "name": "Bhaskar",
                        "roll_number": 104,
                        "branch": "cse",
                        "marks": 91
                    }
                ]

        # insert many records at a time
        collection = mydb['student']
        # collection.insert_many(my_list)

        # # 4. find records
        # # find one record
        # x = collection.find_one()
        # print("record", x)

        # # find all records
        # all_doc = collection.find()
        # for doc in all_doc:
        #     print("doc:", doc)

        # for x in collection.find({}, {"_id": 0, "name": 1, "branch": 1}):
        #     print(x)

        # # Operators in mongodb
        # records = collection.find({"$and": [{"marks": {"$lt": 91}}, {"marks": {"$gt": 80}}]})
        # print("Students who scored more than 90")
        # for record in records:
        #     print("record: %s" % record)

        # sorting of records
        # ascending
        # records = collection.find({"$and": [{"marks": {"$lt": 91}}, {"marks": {"$gt": 80}}]}).sort("name")
        # for record in records:
        #     print("record: %s" % record)

        # # descending
        # records = collection.find({"$and": [{"marks": {"$lt": 91}}, {"marks": {"$gt": 80}}]}).sort("name", -1)
        # for record in records:
        #     print("record: %s" % record)

        # # 5. update
        # roll_filter = {'roll_number': 102}
        # new_values = {"$set": {"marks": 85}}
        # collection.update_one(roll_filter, new_values)

        # upsert ( update and if data is not present then insert it)
        collection.update_many(
            {
                "marks": {
                    "$gt": 40
                }
            },
            {
                "$set": {
                    "passed": "True"
                }
            }
        )

        all_doc = collection.find()
        for doc in all_doc:
            print("doc", doc)

    except ConnectionFailure as e:
        print("error", e)


if __name__ == '__main__':
    main()
