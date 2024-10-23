#!/usr/bin/env python3
"""
This module provides a func to find schs in a MongoDB coll by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents that contain the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)


if __name__ == "__main__":
    pass
