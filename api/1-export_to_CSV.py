#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import requests
import sys


def main():

    employee_id = sys.argv[1]
    employee = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        employee_id)
    name = requests.get(employee).json().get('username')
    request_todo = requests.get(todos).json()

    with open('{}.csv'.format(employee_id), 'w+') as file:
        for todo in request_todo:
            data = '"{}","{}","{}","{}"\n'.format(
                employee_id, name, todo.get('completed'), todo.get('title'))
            file.write(data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
