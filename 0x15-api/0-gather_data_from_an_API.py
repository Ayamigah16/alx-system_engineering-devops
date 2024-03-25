#!/usr/bin/python3
"""
Python script that, using this REST API, for a
given employee ID, returns information about his/her
TODO list progress.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    try:
        response = requests.get(
            f"{base_url}/todos?userId={employee_id}"
        )
        # Raise an exception for HTTP errors
        response.raise_for_status()

        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = sum(
            todo['completed'] for todo in todos
        )
        return total_tasks, completed_tasks, todos
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python3 0-gather_data_from_an_API.py",
            "<employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    total_tasks, completed_tasks, todos = get_employee_todo_progress(
        employee_id)

    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        employee_name = response.json()['name']
    except requests.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)

    print(
        f"Employee {employee_name} is done with ",
        f"tasks({completed_tasks}/{total_tasks}):",
        sep="")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    main()
