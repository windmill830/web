# -*- coding: utf-8 -*-
from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(50)


@app.route('/')
def index():
    session['user'] = 'William'
    return 'Index'


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'


if __name__ == '__main__':
    app.run(debug=True)
