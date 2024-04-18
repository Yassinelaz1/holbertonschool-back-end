#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    username = employee.get("username")
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    data_to_export = {
        employee_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
