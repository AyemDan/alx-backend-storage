#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection.

Functions:
    list_all(mongo_collection: Collection) -> list:
        Lists all documents in the specified MongoDB collection.
"""
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    :param mongo_collection: A pymongo collection object representing the collection 
                              from which to retrieve documents.
    :type mongo_collection: Collection
    :return: A list of documents in the collection, or an empty list if none are found.
    :rtype: list
    :raises ValueError: If the provided mongo_collection is None.
    
    Example:
        collection = db.my_collection
        documents = list_all(collection)
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
