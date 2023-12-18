#!/usr/bin/env python3
"""Using pymongo to interact with mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Inserts values in to a document in the collection"""
    mongo_collection.insert_one(kwargs)
    return mongo_collection.inserted_id
