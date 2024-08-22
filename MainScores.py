from flask import Flask
from Score import read_score

app = Flask(__name__)


@app.route('/')
def hello_world():
    msg = f'<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{read_score()}</div></h1></body></html>'
    return msg

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8777)