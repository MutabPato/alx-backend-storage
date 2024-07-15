#!/usr/bin/env python3
"""NoSQL"""


import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    documents = list(mongo_collection.find())

    return documents if documents else []
