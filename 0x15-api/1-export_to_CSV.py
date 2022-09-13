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
        with open('{}.csv'.format(user['id']), 'w', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in task_list:
                if user['id'] == task['userId']:
                    writer.writerow([
                        user['id'],
                        user['username'],
                        task['completed'],
                        task['title']
                    ])
