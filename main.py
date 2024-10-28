from app import start_play, welcome
from main_score import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/score')
def score():
    try:
        score = score_server()
        return render_template('index.html', score=score)
    except Exception as e:
        return render_template('error.html', error=e)


# welcome()
# start_play()

