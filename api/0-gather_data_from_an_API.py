#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def to_do_list(employee_id):
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()
    info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{employee_id}"
    ).json()
    task_done = [task["title"] for task in todos if task["completed"]]
    print(
        f"Employee {info['name']} is done with tasks\
({len(task_done)}/{len(todos)}):"
    )
    for task in task_done:
        print("\t {}".format(task))


if __name__ == "__main__":
    employee_id = sys.argv[1]
    to_do_list(employee_id)
