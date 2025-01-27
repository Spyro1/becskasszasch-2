from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User, Item, Transaction

routes = Blueprint('routes', __name__)


# Főoldal
@routes.route('/')
def home():
    if request.method == 'POST':
        from .auth import authenticate
        if authenticate():
            pass # Valami történik a user-ral
    return render_template("index.html", user=current_user)

@routes.route('/transactions')
def transactions():
    return render_template("transactions.html", user=current_user, transactions=Transaction.query.all())

@routes.route('/topup')
def top_up():
    return render_template("topup.html", user=current_user, users=User.query.all(), items=Item.query.all())

@routes.route('/users')
def users():
    return render_template("users.html", user=current_user, users=User.query.all())

@routes.route('/items')
def items():
    return render_template("items.html", user=current_user, items=Item.query.all())
