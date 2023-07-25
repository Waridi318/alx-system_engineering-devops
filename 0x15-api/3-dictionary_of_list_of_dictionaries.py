#!/usr/bin/python3
"""
Python script that uses a REST API, fro a given employee id,
returns information about his/her TODO list progress
"""


import json
from requests import get
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    all_users = get(url + "users").json()

    data = {u.get("id"):
            [{"username": u.get("username"),
              "task": t.get("title"),
              "completed": t.get("completed")}
            for t in get(url + "todos",
                         params={"userId": u.get("id")}).json()]
            for u in all_users}
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
