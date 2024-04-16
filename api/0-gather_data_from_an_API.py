#!/usr/bin/python3
import requests
import sys


def to_do_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return

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
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    to_do_list(employee_id)
