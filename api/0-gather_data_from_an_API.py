#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def to_do_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    num_done_tasks = len(done_tasks)
    employee_name = todos[0]['userId'] if todos else "Unknown"

    print(f"Employee {employee_name} is done with tasks"
          f"({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    to_do_list(employee_id)
