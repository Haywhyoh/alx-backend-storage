#!/usr/bin/env python3
"""Change school topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name """
    my_query = {"name": name}
    newvalues = {"$set": {"topic": topics}}
    mongo_collection.update_many()
