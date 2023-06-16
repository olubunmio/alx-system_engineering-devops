#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    if len(argv) < 2:
        print("USAGE:  {}  <employee_id>".format(argv[0]))
    else:
        # Fetch employee's personal details
        r = get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        )
        # Store employee's name
        employee_username = r.json().get('username')

        # Fetch employee's todo list
        r = get('https://jsonplaceholder.typicode.com/todos/')
        # Process Todo
        tmp_lst = r.json()
        all_todo_items = []

        for item in tmp_lst:
            if item.get('userId') == int(argv[1]):
                status = item.get('completed')
                title = item.get('title')
                all_todo_items.append('"{}","{}","{}","{}"\n'.format(
                    argv[1], employee_username, status, title)
                )

        # Write to a `.csv` file
        with open("{}.csv".format(argv[1]), 'w') as fhand:
            fhand.writelines(all_todo_items)
