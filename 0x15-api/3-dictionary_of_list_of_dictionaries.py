#!/usr/bin/python3
"""Export to json"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # get url
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(argv[1]))

    data_dict = {}

    for u_name in user_list:
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(u_name['id']))
        todo_list = todo.json()

        data_list = []

        # create a new dict with the user items
        for data in todo_list:
            user_task = {}
            user_task["username"] = u_name['username']
            user_task["task"] = data['title']
            user_task["completed"] = data['completed']
            data_list.append(user_task)

        data_dict[u_name['id']] = data_list

    # json file name
    json_file = 'todo_all_employees.json'

    # insert items in file
    with open(json_file, mode='w') as jfile:
        json.dump(data_dict, jfile)
