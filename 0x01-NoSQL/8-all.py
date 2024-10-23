#!/usr/bin/env python3
"""
A module providing afunc to list all docs in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all docs in collection. Returns empty list if no docs found.
    """
    documents = mongo_collection.find()
    return list(documents) if documents.count() > 0 else []


if __name__ == "__main__":
    pass
