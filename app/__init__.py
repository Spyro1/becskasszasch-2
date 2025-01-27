from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

# Konstansok
DB_NAME = 'database.db'
FOLDER_NAME = 'website'

app = Flask(__name__) # Flask app létrehozása
db = SQLAlchemy() # Adatbázis létrehozása


def create_app():

    app.config['SECRET_KEY'] = 'SOME SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQLite adatbázis konfigurálása

    db.init_app(app) # Inizializáljuk az adatbázist az appal

    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/') # endpointok hozzáakpcsolása az apphoz
    app.register_blueprint(auth, url_prefix='/') # authentikációs endpointok hozzákapcsolása

    from .models import User, Item, Transaction # Importáljuk a modellek fájlt, hogy az adatbázis számára be legyen töltve
    # import models as models

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists(f'./instance/{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print('Database created!')
    else:
        print('Database already exists')
        