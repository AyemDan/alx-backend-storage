#!/usr/bin/env python3
""" 
This module provides a function to retrieve and sort students
by their average scores from a MongoDB collection.

Functions:
top_students(mongo_collection: Collection) -> List[Dict]:
"""

from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    """
    Retrieves all students from the given MongoDB collection, calculates their average scores,
    and returns a list of students sorted by their average scores in descending order.
    
    Args:
        mongo_collection (Collection): The MongoDB collection containing student documents.
    
    Returns:
        List[Dict]: A list of student documents with an additional field "averageScore",
                    sorted by "averageScore" in descending order.
    """

    return mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,  # Include name in the result
                "averageScore": {
                    "$avg": {
                        "$map": {
                            "input": "$topics",  # The array of topics
                            "as": "topic",       # Temporary variable for each element in the array
                            "in": "$$topic.score" # Extract the 'score' field from each topic
                        }
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$name",  # Group by student name
                "averageScore": {"$first": "$averageScore"}  # Take the first averageScore value (since grouped by name)
            }
        },
        {
            "$sort": {
                "averageScore": -1  # Sort by averageScore in descending order
            }
        }
    ])
