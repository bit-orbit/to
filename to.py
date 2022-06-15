import json
import os
import errors
import core


board_path = '.to/board.json'
board = None

assert os.path.exists(board_path), errors.FILE_NOT_EXIST

with open(board_path, 'r') as fli:
    board = core.Tools().dict2object(json.load(fli))

print(board)
