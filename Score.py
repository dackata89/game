import os
from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points = (difficulty * 3 ) + 5

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read().strip())
            file.close()

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(current_score + points))
            file.close()
    else:
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(points))
            file.close()

def read_score():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read().strip())
            file.close()
    else:
        current_score = 0

    return current_score