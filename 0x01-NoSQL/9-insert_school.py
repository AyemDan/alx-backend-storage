#!/usr/bin/env python3
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on the provided keyword arguments.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the document fields to insert.

    Returns:
        The _id of the newly inserted document.
    """
    if not kwargs:
        raise ValueError("No fields provided to insert.")
    
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id