#!/usr/bin/env python3
"""
This module provides a function to insert a new doc into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the doc to insert.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    pass
