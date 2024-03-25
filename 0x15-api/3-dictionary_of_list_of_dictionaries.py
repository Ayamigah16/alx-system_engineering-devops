#!/usr/bin/python3
"""Export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users").json()
    user_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = requests.get(
            f"{url}/todos?userId={user_id}").json()
        task_list = []

        for task in tasks:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            task_list.append(task_dict)

        user_tasks[user_id] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)
