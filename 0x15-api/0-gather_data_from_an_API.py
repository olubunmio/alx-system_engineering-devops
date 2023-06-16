#!/usr/bin/python3
""" A python script that using the REST API at
`https://jsonplaceholder.typicode.com/{users,todos}/` for a given
employee ID, returns information about his/her TODO list progress
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("USAGE:  {}  <employee_id>".format(argv[0]))
    else:
        # Fetch employee's personal details
        r = get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        )
        # Store employee's name
        employee_name = r.json().get('name')

        # Fetch employee's todo list
        r = get('https://jsonplaceholder.typicode.com/todos/')
        # Process Todo
        tmp_lst = r.json()
        all_todo_items = []
        done_items = []
        for item in tmp_lst:
            if item.get('userId') == int(argv[1]):
                all_todo_items.append(item)
                if item.get('completed') is True:
                    done_items.append(item)

        # Pretty print te result
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_items), len(all_todo_items)))
        for item in done_items:
            print('\t {}'.format(item.get('title')))
