#!/usr/bin/env python3
"""
This module provides a func to return all students sorted by their avg score.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of student documents sorted by their average score, 
        with each document containing the key 'averageScore'.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))


if __name__ == "__main__":
    pass
