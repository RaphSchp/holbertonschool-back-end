#!/usr/bin/python3
"""
Module returns information about his/her TO_DO list progress
when an employee ID is provided as argument.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Returns information about his/her TODO list progress.
    """
    # Get the user name through the API
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()  # Parse user names to JSON
    employee_name = user_data['name']


#  Get the user's tasks through the API
    todo_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employee_id))
    todo_data = todo_response.json()  # Parse user's tasks to JSON
    total_tasks = len(todo_data)  # Get the total number of tasks


# Get the number of completed tasks
    done_tasks = [task for task in todo_data if task['completed'] is True]
    num_done_tasks = len(done_tasks)  # Get  the number of completed tasks

# Print the user's tasks
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))


# Save the information in the JSON file
    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump({employee_id: [{
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        } for task in todo_data]}, jsonfile)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
