#!/usr/bin/python3
""" Module using REST API that returns info of to-do list
    and records it in CSV Format """

import csv
import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit() is True:
        match_id = int(sys.argv[1])

        """ Gets user corresponding to id passed as command line argument """
        response1 = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(match_id))
        user = json.loads(response1.text)

        """ Gets list of all tasks available in the to-do list """
        response2 = requests.get('https://jsonplaceholder.typicode.com/todos')
        task_list = json.loads(response2.text)

        """ Exports formatted info to CSV format """
        with open('{}.json'.format(user['id']), 'w', encoding='utf-8') as f:
            task_dict = {}
            tasks = []
            for task in task_list:
                task_dict["task"] = task['title']
                task_dict["completed"] = task['completed']
                task_dict["username"] = user['username']
                tasks.append(task_dict)
            user_info = {user['id']: tasks}
            json.dump(user_info, f)
