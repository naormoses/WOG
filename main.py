from app import start_play, welcome
from main_score import *
from flask import Flask, render_template, request
from e2e import *

app = Flask(__name__)

@app.route("/")
def Hello_User():
    return ("<p>Hello And Welcome to My World Of Games: The Epic Journey \n"
            "Please Move to '/Score' to see your score. </p>")

@app.route('/score')
def score():
    try:
        score = score_server()
        return render_template('index.html', score=score)
    except Exception as e:
        return render_template('error.html', error=e)
    
# test_scores_service('http://localhost:5000/scores')