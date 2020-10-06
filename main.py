import os
import math
import sys
import datetime
import flask
from flask import request, jsonify, render_template

app=flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route("/",methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route("/login",methods=['POST','GET'])
def homely():
    return render_template("login.html")


@app.route("/api/v1/resources/books/all", methods=['GET'])
def api_all():
    return jsonify(books)

@app.route("/form-end", methods=['POST'])
def formend():
    return "Mpop"

@app.route("/login/register", methods=['POST'])
def login():
    data_to_check=request.get_json(force=True)
    if (data_to_check['name']=='jayesh' and data_to_check['password']=='jayesh'):
        return render_template("")

    


# @app.route("/account/balance", methods=['POST'])


# @app.route("/account/withdraw", methods=['POST'])


# @app.route("/account/deposit", methods=['POST'])


app.run()
