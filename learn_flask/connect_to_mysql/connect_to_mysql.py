# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/sqlalchemytest?charset=utf8'
db = SQLAlchemy(app)


class Connect(db.Model):
    __tablename__ = 'connect_example'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))


if __name__ == '__main__':
    app.run(debug=True)
