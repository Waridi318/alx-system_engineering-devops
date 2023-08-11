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
    url = f'https://jsonplaceholder.typicode.com/'
    params = {"userId": argv[1]}

    tasks = get(url + "todos", params).json()
    name = get(url + f"users/{argv[1]}").json()
    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print(f"Employee {name.get('name')} is done with tasks"
          f"({len(completed)}/{len(tasks)}):")
    for c in completed:
        print(f"\t {c}")
