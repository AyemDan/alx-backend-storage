#!/usr/bin/env python3
"""
This module provides a function to update the topics field of a document in a MongoDB collection.

Functions:
    update_topics(mongo_collection: Collection, name: str, topics: list) -> None:
        Updates the topics field of a school document in the collection based on the school name.
"""

def update_topics(mongo_collection, name: str, topics: list):
    """
    Updates the topics for a school document in the collection based on the provided name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school whose topics need to be updated.
        topics (list): A list of strings representing the new topics to set.

    Returns:
        None

    Raises:
        ValueError: If the name or topics parameters are invalid (e.g., empty or not of the expected type).
    Notes:
        - If no document matches the provided name, the update operation will have no effect.
        - Ensure that the `mongo_collection` object is properly connected to a MongoDB instance.

    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("The name parameter must be a non-empty string.")
    
    if not isinstance(topics, list) or not all(isinstance(topic, str) for topic in topics):
        raise ValueError("The topics parameter must be a list of strings.")
    
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
