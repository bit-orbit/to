import json
import os
import errors
import core


board_path = '.to/board.json'
board = None

assert os.path.exists(board_path), errors.FILE_NOT_EXIST

with open(board_path, 'r') as fli:
    board = json.load(fli)
    listed_tasks = core.getAllListedTasks(board)

for listed_task in listed_tasks:
    for task in listed_tasks.get(listed_task):
        print(listed_task, task['name'])
