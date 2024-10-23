#!/usr/bin/env python3
"""
This module provides a func to update the topics of a sch doc in a MongoDB coll
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a sch doc in MongoDB collection based on sch name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of strings representing the topics to update.

    Returns:
        None..
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == "__main__":
    pass
