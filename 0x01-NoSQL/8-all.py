#!/usr/bin/env python3
""" 
This module provides a function to list all documents in a MongoDB collection.
Functions:
    list_all(mongo_collection: Collection) -> list: 
    """

from pymongo.collection import Collection


def list_all(mongo_collection: Collection):
    """
    Lists all documents in a MongoDB collection.

    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection, or an empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
