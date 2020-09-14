#!/usr/bin/python3
"""script that returns information about his/her TODO list progress"""

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

    total_tasks = 0
    tasks_done = 0
    task_title = []

    # run into key to take values
    for tasks in todo_list:
        if tasks['completed'] is True:
            tasks_done += 1
            task_title.append(tasks['title'])
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_list['name'], tasks_done, total_tasks))

    for list in task_title:
        print("\t {}".format(list))
