#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be:
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""
from requests import get
import json

if __name__ == "__main__":
    # Fetch all employees' personal details
    r_users = get('https://jsonplaceholder.typicode.com/users/')

    # Fetch employee's todo list
    r_todos = get('https://jsonplaceholder.typicode.com/todos/')
    # Process Todo
    tmp_users_lst = r_users.json()
    tmp_todos_lst = r_todos.json()

    result = {}
    for user in tmp_users_lst:
        value = []

        username = user.get('username')
        id = user.get('id')

        for todo in tmp_todos_lst:
            if todo.get('userId') == id:
                task = todo.get('title')
                completed = todo.get('completed')
                value.append({"username": username, "task": task,
                              "completed": completed})
        result[id] = value

    # Write to a `.json` file
    with open('todo_all_employees.json', 'w') as fhand:
        json.dump(result, fhand)
