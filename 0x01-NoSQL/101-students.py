#!/usr/bin/env python3
"""NoSQL"""


import pymongo
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averagescore": -1}}
    ])
