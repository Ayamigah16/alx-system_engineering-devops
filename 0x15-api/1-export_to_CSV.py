#!/usr/bin/python3
"""
Extend your 0-gather_data_from_an_API.py to
export data in the CSV format
"""

import sys
import requests
import csv


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


def export_to_csv(employee_id, todos):
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        employee_name = response.json()['name']
        file_name = f"{employee_id}.csv"
        with open(file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(
                ["USER_ID", "USERNAME",
                 "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos:
                csv_writer.writerow(
                    [employee_id, employee_name,
                     str(todo['completed']), todo['title']])
        print(f"Data exported to {file_name}")
    except requests.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todos = get_employee_todo_progress(employee_id)
    export_to_csv(employee_id, todos)


if __name__ == "__main__":
    main()
