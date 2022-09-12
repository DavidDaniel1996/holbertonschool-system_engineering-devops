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

        """ Gets total number of tasks related to user,
        amount of those tasks that are done, and the names of those tasks """
        total_tasks = 0
        tasks_done = 0
        task_names = []
        for task in task_list:
            if user['id'] == task['userId']:
                total_tasks += 1
                if task['completed'] is True:
                    task_names.append(task['title'])
                    tasks_done += 1

        """ Prints all information gathered in a specific format """
        print('Employee {} is done with tasks({}/{}):'
              .format(user['name'], tasks_done, total_tasks))
        for title in task_names:
            print('\t {}'.format(title))
