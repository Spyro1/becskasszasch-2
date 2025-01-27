from flask import Blueprint, render_template

endpoints = Blueprint('endpoints', __name__)


# Főoldal
@endpoints.route('/')
def home():
    return render_template("home.html", user=None) # None átírandó


# Login request
@endpoints.route('/login')
def login():
    from .auth import authenticate
    return authenticate()
    # return render_template('home.html', user='Login in progress')