#!/usr/bin/python3
"""
Module returns information about his/her TO_DO list progress
when an employee ID is provided as argument.
"""
import json
import requests
import sys


def export_all_to_json():
    user_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = user_response.json()

    all_tasks = {}
    for user in users_data:
        employee_id = user['id']
        employee_name = user['name']

        todos_response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(employee_id))
        todos_data = todos_response.json()

        tasks = []
        for task in todos_data:
            tasks.append({
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            })

        all_tasks[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
