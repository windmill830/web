# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def url_for_test():
    return render_template('url_for test.html')


@app.route('/page')
def page_link():
    return 'On Page'


@app.route('/page/<string:user>')
def user_page(user):
    return 'User: ' + user

if __name__ == '__main__':
    app.run(debug=True)
