#!/usr/bin/env python3
"""NoSQL"""


import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['logs']
collection = db['nginx']

print(f"{db.collection.count_documents({})} logs")
print('Methods:')
print(f'\tmethod GET: {db.collection.count_documents({"method": "GET"})}')
print(f'\tmethod POST: {db.collection.count_documents({"method": "POST"})}')
print(f'\tmethod PUT: {db.collection.count_documents({"method": "PUT"})}')
print(f'\tmethod PATCH: {db.collection.count_documents({"method": "PATCH"})}')
print(f'\tmethod DELETE: {db.collection.count_documents({"method": "DELETE"})}')
print(f'{db.collection.count_documents({"method": "GET", "path": "/status"})} status check')
