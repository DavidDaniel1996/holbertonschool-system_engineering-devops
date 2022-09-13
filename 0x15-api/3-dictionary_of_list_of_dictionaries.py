#!/usr/bin/python3
""" Module using REST API that returns info of to-do list
    and records it in CSV Format """

import csv
import json
import requests
import sys

if __name__ == "__main__":

    """ Gets user corresponding to id passed as command line argument """
    response1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    users = json.loads(response1.text)

    """ Gets list of all tasks available in the to-do list """
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos')
    task_list = json.loads(response2.text)

    """ Exports formatted info to JSON file """
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        users_info = {}
        for user in users:
            task_dict = {}
            tasks = []
            for task in task_list:
                if user['id'] == task['userId']:
                    task_dict['username'] = user['username']
                    task_dict['task'] = task['title']
                    task_dict['completed'] = task['completed']
                    dict_copy = task_dict.copy()
                    tasks.append(dict_copy)
            users_info[user['id']] = tasks
        json.dump(users_info, f)
