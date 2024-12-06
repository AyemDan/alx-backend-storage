#!/usr/bin/env python3
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic):
    """
    Returns a list of schools that have the specified topic.

    :param mongo_collection: pymongo collection object
    :param topic: string, the topic to search for
    :return: list of school names that have the given topic
    """
    # Find schools that have the topic in the 'topics' list
    schools = mongo_collection.find({"topics": topic})

    return schools
