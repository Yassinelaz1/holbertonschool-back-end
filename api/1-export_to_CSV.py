#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import csv
import requests
import sys


def TODO_REQUESTS(ID):
    """
    extend your Python script to export data in the CSV format
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    with open(f"{ID}.csv", mode="w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [(ID), user_info["username"],
                 todo["completed"], todo["title"]]
            )


if __name__ == "__main__":
    ID = sys.argv[1]
    TODO_REQUESTS(ID)
