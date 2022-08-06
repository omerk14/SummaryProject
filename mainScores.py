from flask import Flask
from utils import  get_scores_file_name

app = Flask(__name__)

@app.route('/getScores')
# ‘/’ URL is bound with hello_world() function.
def score_server():
    try:
        score = open(get_scores_file_name()).read()
        msg = "<html> \
<head> \
<title>Scores Game</title> \
</head> \
<body> \
<h1>The score is <div id=\"score\">{}</div></h1> \
</body>\
</html>".format(score)
        return msg
    except:
        msg = "<html> \
<head> \
<title>Scores Game</title> \
</head> \
<body> \
<body> \
<h1><div id=\"score\" style=\"color:red\">{ERROR}</div></h1> \
</body> \
</html>"
        return msg


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()