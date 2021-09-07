#!/usr/bin/env python3
''' lists all documents in a collection '''


def list_all(mongo_collection):
    ''' list all documents in the collection'''
    return mongo_collection.find()
