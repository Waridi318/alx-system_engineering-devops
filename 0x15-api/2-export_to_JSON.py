#!/usr/bin/python3
"""
Python script that uses a REST API, fro a given employee id,
returns information about his/her TODO list progress
"""


import json
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    params = {"userId": argv[1]}

    tasks = get(url + "todos", params).json()
    name = get(url + f"users/{argv[1]}").json()
    username = name.get("username")
    completed = [t.get("title") for t in tasks if t.get("completed") is True]

    data = {user_id: [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username
                       } for t in tasks]}
    file_name = f'{user_id}.json'
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
