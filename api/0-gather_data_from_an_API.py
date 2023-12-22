#!/usr/bin/python3
"""This script fetches and displays the TODO list progress for a
given employee ID."""

import requests
from sys import argv


def get_employee_todo_progress():
    """Fetch and print TODO list progress for a given user_id."""

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()
        user_name = user["name"]

    url_todos = (
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')

    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    print("Employee {} is done with tasks ({}/{}):"
          .format(user_name, done_tasks, total_tasks))

    task_titles = [todo['title'] for todo in todos if todo['completed']]
    for title in task_titles:
        print("\t {}".format(title))


if __name__ == '__main__':
    get_employee_todo_progress()
