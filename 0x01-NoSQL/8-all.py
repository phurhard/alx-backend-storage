#!/usr/bin/env python3
"""Using pymongo to interact with mongo"""


def list_all(mongo_collection):
    """This returns all the documents in the mongo db"""
    query = mongo_collection.find()
    if query is None:
        return []
    return query
