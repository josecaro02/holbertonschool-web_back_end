#!/usr/bin/env python3
''' inserts a new document in a collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
    ''' inserts base in kwargs in the collection'''
    itemInsert = {}
    for key, value in kwargs.items():
        itemInsert[key] = value
    itemID = mongo_collection.insert_one(itemInsert)
    return itemID
