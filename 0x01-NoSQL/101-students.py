#!/usr/bin/env python3
"""Using pymongo to interact with the mongodb"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    mongo_collection.find().sort("averageScore", pymongo.ASCENDING)
    