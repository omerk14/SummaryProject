import os

SCORES_FILE_NAME = "C:\\Users\\User\\SummaryProject\\scores.txt"
BAD_RETURN_CODE = 1

def Screen_cleaner():
    os.popen("cls")

def get_scores_file_name():
    try:
        with open(SCORES_FILE_NAME) as f:
            return SCORES_FILE_NAME
    except FileNotFoundError:
        f = open(SCORES_FILE_NAME,"w")
        print("Create new scores file")
        return SCORES_FILE_NAME
    # if  contents == 0:
    #     print (f.read())
    #     return SCORES_FILE_NAME
    # else:
    #     return "No such file"

if __name__ == '__main__':
    print("hi")