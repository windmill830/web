# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    user = User.query.filter_by(name='Doe').first()
    login_user(user)
    return 'You are now logged in!'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'


@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.name

if __name__ == '__main__':
    app.run(debug=True)
