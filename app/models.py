from . import db
from flask_login import UserMixin
# from enum import Enum


# class Rank(Enum):
#     User = 1
#     Bartender = 2
#     Admin = 3

class User(db.Model, UserMixin):
    schacc = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    balance = db.Column(db.Integer, default=0)
    credit = db.Column(db.Integer, default=5000)
    isadmin = db.Column(db.Boolean, default=False)
    # spendings = db.relationship('Transaction')

    def __repr__(self):
        return f'<User {self.schacc} | {self.name}>'
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    icon_uri = db.Column(db.String(200), nullable=False)
    isactive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Item id:{self.id} | {self.name}, {self.price}, {self.isactive}>'
    
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schacc = db.Column(db.String(150), db.ForeignKey('user.schacc'), nullable=False)
    item_id = db.Column(db.String(150), db.ForeignKey('item.id'), nullable=False)
    amount = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f'<Transaction id:{self.id} | {self.schacc} - {self.item_id} | {self.amount}>' % self.id
    
    