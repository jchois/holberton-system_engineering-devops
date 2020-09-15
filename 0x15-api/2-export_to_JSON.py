#!/usr/bin/python3
"""Export to CSV"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # get url
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(argv[1]))

    # convert to json
    user_list = users.json()
    todo_list = todo.json()

    data_dict = {}
    data_list = []

    # create json file
    json_file = argv[1] + '.json'

    # creating a dict inside a list
    for data in todo_list:
        user_task = {}
        user_task["task"] = data['title']
        user_task["completed"] = data['completed']
        user_task["username"] = user_list['username']
        data_list.append(user_task)

    # create a list inside a dict
    data_dict[argv[1]] = data_list

    # open csv file
    with open(json_file, mode='w') as jfile:
        json.dump(data_dict, jfile)
