#!/usr/bin/env python3
"""
This module provides a function to insert a new document into a MongoDB collection.

Functions:
    insert_school(mongo_collection: Collection, **kwargs) -> Any:
        Inserts a new document into the specified MongoDB collection using the provided fields.
"""

from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on the provided keyword arguments.

    Args:
        mongo_collection (Collection): A pymongo collection object representing the target collection.
        **kwargs: Key-value pairs representing the fields and their values for the new document.

    Returns:
        Any: The `_id` of the newly inserted document.

    Raises:
        ValueError: If no keyword arguments are provided.

    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://localhost:27017/')
        >>> db = client.my_database
        >>> collection = db.schools
        >>> new_id = insert_school(collection, name="ABC School", location="New York")
        >>> print(new_id)

    Notes:
        - Ensure the collection object is connected to a valid MongoDB instance before calling this function.
        - The `_id` is automatically generated unless provided explicitly in the `kwargs`.
    """
    if not kwargs:
        raise ValueError("No fields provided to insert.")
    
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
