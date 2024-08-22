import os

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')