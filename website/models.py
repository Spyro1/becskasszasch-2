from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    schacc = db.Column(db.String(300), primary_key=True, unique=True)
    name = db.Column(db.String(150))
    balance = db.Column(db.Integer, default=0)
    credit = db.Column(db.Integer, default=5000)
    isadmin = db.Column(db.Boolean, default=False)
    # spendings = db.relationship('Transaction')
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Integer)
    icon_uri = db.Column(db.String(150))
    isactive = db.Column(db.Boolean, default=True)
    
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schacc = db.Column(db.String(150), db.ForeignKey('user.schacc'))
    item_id = db.Column(db.String(150), db.ForeignKey('item.id'))
    amount = db.Column(db.Integer)
    
    