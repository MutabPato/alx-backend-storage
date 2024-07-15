#!/usr/bin/env python3
"""NoSQL"""


import pymongo
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    result = list(mongo_collection.find({"topics": topic}))
    return result
