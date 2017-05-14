# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Connect(db.Model):
    __tablename__ = 'connect_example'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))

if __name__ == '__main__':
    app.run(debug=True)
