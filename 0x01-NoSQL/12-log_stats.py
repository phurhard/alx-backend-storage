#!/usr/bin/env python3
"""using pymongo to interact with the mongodb"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Function is used to print tables"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    numOfDocument = collection.count_documents({})
    documentsWithGET = collection.count_documents({"method": "GET"})
    documentsWithPOST = collection.count_documents({"method": "POST"})
    documentsWithPUT = collection.count_documents({"method": "PUT"})
    documentsWithPATCH = collection.count_documents({"method": "PATCH"})
    documentsWithDELETE = collection.count_documents({"method": "DELETE"})
    documentSuccess = collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{numOfDocument} logs')
    print('Methods:')
    print(f'\tmethod GET: {documentsWithGET}')
    print(f'\tmethod POST: {documentsWithPOST}')
    print(f'\tmethod PUT: {documentsWithPUT}')
    print(f'\tmethod PATCH: {documentsWithPATCH}')
    print(f'\tmethod DELETE: {documentsWithDELETE}')
    print(f'{documentSuccess} status check')
