#!/usr/bin/python3
"""Exports data in CSV format
"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    file_name = userId + '.csv'

    with open(file_name, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')

        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
