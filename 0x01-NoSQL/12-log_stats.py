#!/usr/bin/env python3
"""NoSQL"""


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['logs']

collection = db['nginx']

print(f'{collection.count_documents({})} logs')
print('Methods:')
print(f'\tmethod GET: {collection.count_documents({"method": "GET"})}')
print(f'\tmethod POST: {collection.count_documents({"method": "POST"})}')
print(f'\tmethod PUT: {collection.count_documents({"method": "PUT"})}')
print(f'\tmethod PATCH: {collection.count_documents({"method": "PATCH"})}')
print(f'\tmethod DELETE: {collection.count_documents({"method": "DELETE"})}')
status = collection.count_documents({"method": "GET", "path": "/status"})
print(f'{status} status check')
