#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    """Get the response and format and write data to CSV"""

    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()

    username = user.get("username")
    data_user = []

    for todo in todos:
        newrow = [todo.get("userId"), username, todo.get("completed"),
                  todo.get("title")]
        data_user.append(newrow)

    file_name = '{}.csv'.format(argv[1])
    with open(file_name, mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(data_user)

        print(f"Data has been exported to {argv[1]}.csv")
