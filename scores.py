import os
from utils import  get_scores_file_name

POINTS_OF_WINNING = 0

def add_score(difficulty):
    f = open(get_scores_file_name(),"r")
    temp = f.read()
    score =  int(temp) + (difficulty * 3) + 5
    f.close()
    f = open(get_scores_file_name(),"w")
    f.write(str(score))
    f.close()
    print(get_scores_file_name())

if __name__ == '__main__':
    print(add_score(2))