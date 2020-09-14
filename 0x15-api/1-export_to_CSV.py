#!/usr/bin/python3
"""Export to CSV"""

import csv
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

    filename = argv[1] + '.csv'

    # creating a csv file
    with open(filename, mode='w') as file:
        csv_data = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        # insert items to csv file
        for item in todo_list:
            csv_data.writerow([item['userId'], user_list['username'],
                              item['completed'], item['title']])
