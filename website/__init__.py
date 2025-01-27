from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Konstansok
DB_NAME = 'database.db'
FOLDER_NAME = 'website'


db = SQLAlchemy()

def create_app():
    app = Flask(__name__) # Flask app létrehozása
    
    app.config['SECRET_KEY'] = 'SOME SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQLite adatbázis konfigurálása

    # db =  SQLAlchemy(app) # Adatbázis létrehozása
    db.init_app(app) # Inizializáljuk az adatbázist az appal

    from .endpoints import endpoints
    app.register_blueprint(endpoints, url_prefix='/') # endpointok hozzáakpcsolása az apphoz
    
    from .models import User, Item, Transaction # Importáljuk a modellek fájlt, hogy az adatbázis számára be legyen töltve 
    # import models as models

    create_database(db, app)

    return app

def create_database(db, app):
    if not path.exists(f'./instance/{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print('Database created!')
    else: print('Database already exists')
        