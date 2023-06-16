#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:
Records all tasks that are owned by this employee
Format must be:
{ "USER_ID": [{"task": "TASK_TITLE", "completed":TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

File name must be: USER_ID.json
"""
from requests import get
from sys import argv
import json

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
                tmp_dict = {}
                tmp_dict['task'] = item.get('title')
                tmp_dict['completed'] = item.get('completed')
                tmp_dict['username'] = employee_username
                all_todo_items.append(tmp_dict)

        # Write to a `.json` file
        with open("{}.json".format(argv[1]), 'w') as f:
            json.dump({argv[1]: all_todo_items}, f)
