#!/usr/bin/env python3
"""Using pymongo to interact with the mongodb"""


def schools_by_topic(mongo_collection, topic):
    """Returns the schools with the search query"""
    return mongo_collection.find({"topics": topic})
