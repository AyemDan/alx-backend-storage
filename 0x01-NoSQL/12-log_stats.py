#!/usr/bin/env python3

"""
This script connects to a MongoDB database and retrieves statistics from an Nginx log collection.

Functions:
    get_nginx_log_stats():
        Retrieves and prints statistics about the Nginx logs, including total log count,
        method usage, and counts for specific endpoints like "GET /status".
"""

from pymongo import MongoClient


def get_nginx_log_stats():
    """
    Connects to the MongoDB instance and retrieves statistics about the Nginx logs.

    The script provides:
        - Total number of logs.
        - Counts of logs for each HTTP method.
        - Count of "GET" requests to the "/status" path.

    MongoDB Assumptions:
        - Database: "logs"
        - Collection: "nginx"
        - Documents have fields "method" and optionally "path" for HTTP methods and endpoints.

    Returns:
        None: Prints the log statistics to the console.
    """
 
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    status_logs = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"GET /status: {status_logs}")


if __name__ == "__main__":
    get_nginx_log_stats()
