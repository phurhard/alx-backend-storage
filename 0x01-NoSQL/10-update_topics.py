#!/usr/bin/env python3
"""Using pymongo to interact with the mongodb"""


def update_topics(mongo_collection, name, topics):
    """Updates the school with the query filter"""
    update_data = {"name": name}
    update_topics = {"$set": {"topics": topics}}
    mongo_collection.update_one(update_data, update_topics)
