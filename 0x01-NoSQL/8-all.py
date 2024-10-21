#!/usr/bin/env python3
"""NoSQL"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in Python"""
    return mongo_collection.find()
