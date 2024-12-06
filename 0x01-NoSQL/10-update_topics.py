#!/usr/bin/env python3
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name, topics):
    """
    Updates the topics for a school document in the collection based on the name.

    :param mongo_collection: pymongo collection object
    :param name: string, the name of the school to update
    :param topics: list of strings, the new topics to update for the school
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}} 
    )