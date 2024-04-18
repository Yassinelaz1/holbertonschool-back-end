#!/usr/bin/python3
"""export data in the JSON format."""

import json
import requests


def fetch_user_data():
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users").json()

    data_to_export = {}
    for user in employee:
        employee_id = user["id"]
        user_url = url + f"todos?userId={employee_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[employee_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
