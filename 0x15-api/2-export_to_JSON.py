#!/usr/bin/python3
"""Exports data in JSON format
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    todos = todos.json()
    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)

    todoUser[userId] = taskList

    file_name = userId + '.json'

    with open(file_name, mode='w') as f:
        json.dump(todoUser, f)
