#!/usr/bin/env python3
"""
This module provides a function to retrieve schools based on a specific topic.

Functions:
    schools_by_topic(mongo_collection: Collection, topic: str) -> list:
        Returns a list of schools that include the specified topic.
"""

from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic: str) -> list:
    """
    Returns a list of schools that have the specified topic in their 'topics' field.

    Args:
        mongo_collection (Collection): The pymongo collection object representing the schools collection.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        list: A list of dictionaries representing the schools that have the specified topic.

    Raises:
        ValueError: If the topic parameter is not a non-empty string
    Notes:
        - The 'topics' field in each school document is expected to be a list of strings.
        - The function performs a case-sensitive search.
    """
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("The topic parameter must be a non-empty string.")

    # Find schools where the topic exists in the 'topics' field
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
