#!/usr/bin/python3
import csv
import requests
import sys



def to_do_list(employee_id):

    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()
    response = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{employee_id}"
    ).json()
    with open(f"{employee_id}.csv", mode="w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [(employee_id), response["username"],
                 todo["completed"], todo["title"]]
            )


if __name__ == "__main__":
    employee_id = sys.argv[1]
    to_do_list(employee_id)
