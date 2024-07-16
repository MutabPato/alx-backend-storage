#!/usr/bin/env python3
"""NoSQL"""


import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']

    print(f"{collection.count_documents({})} logs")
    print('Methods:')
    print(f'\tmethod GET: {collection.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {collection.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {collection.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {collection.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: '
          f'{collection.count_documents({"method": "DELETE"})}')
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})}'
          f' status check')
    print("IPs:")
    sorted_ips = collection.aggregate(
            [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
             {"$sort": {"count": -1}}])
    i = 0
    for s in sorted_ips:
        if i == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        i += 1
