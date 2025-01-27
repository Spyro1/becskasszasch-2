from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(schacc=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Sikeres bejelentkezés!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash('Helytelen jelszó, próbáld újra.', category='error')
        else:
            flash('Felhasználó nem létezik.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_again = request.form.get('password-again')
        isadmin = request.form.get('isadmin')

        user = User.query.filter_by(schacc=username).first()

        if user:
            flash('Felhasználó már létezik.', category='error')
        elif len(username) < 5:
            flash('A felhasználónévnek legalább 5 karakter hosszúnak kell lennie.', category='error')
        elif password != password_again:
            flash('A jelszavak nem eggyeznek.', category='error')
        elif len(password) < 5:
            flash('A jelszónak legalább 5 karakternek kell lennie.', category='error')
        else:
            new_user = User(schacc=username+'-schacc', name=username, password=generate_password_hash(password, method='pbkdf2:sha256'), isadmin=True if isadmin else False)
            db.session.add(new_user)
            db.session.commit()
            # login_user(new_user, remember=True)
            login_user(new_user)
            flash('Felhasználó létrehozva!', category='success')
            return redirect(url_for('views.home'))
    return render_template("register.html", user=current_user)