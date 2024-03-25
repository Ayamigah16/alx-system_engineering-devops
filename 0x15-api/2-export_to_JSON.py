#!/usr/bin/python3
"""
Extend your 0-gather_data_from_an_API.py
to export data in the JSON format.
"""

import sys
import requests
import json


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    try:
        response = requests.get(
            f"{base_url}/todos?userId={employee_id}")
        response.raise_for_status()
        # Raise an exception for HTTP errors

        todos = response.json()
        return todos
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def export_to_json(employee_id, todos):
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        employee_name = response.json()['name']
        file_name = f"{employee_id}.json"
        data = {
            employee_id: [
                {"task": todo['title'],
                 "completed": todo['completed'],
                 "username": employee_name} for todo in todos]}
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data exported to {file_name}")
    except requests.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todos = get_employee_todo_progress(employee_id)
    export_to_json(employee_id, todos)


if __name__ == "__main__":
    main()
