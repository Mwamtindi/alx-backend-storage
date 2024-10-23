#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx

    # Get the total num of logs
    total_logs = nginx_collection.count_documents({})

    # Define the HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Print the total num of logs
    print(f"{total_logs} logs")

    # Print method counts
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the num of GET requests to /status
    status_check =
    nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
