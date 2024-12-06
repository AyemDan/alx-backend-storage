#!/usr/bin/env python3

from pymongo import MongoClient

def get_nginx_log_stats():
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

get_nginx_log_stats()
