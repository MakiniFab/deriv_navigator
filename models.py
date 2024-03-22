#import needed dependancies
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

#users model
class User(db.Model, SerializerMixin):
    serialize_only = ('id', 'first_name', 'account', 'email', 'phone_no')
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    account = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    phone_no = db.Column(db.Integer, unique=True) 
    admin = db.Column(db.Boolean, default=False) 
    password = db.Column(db.String)

#blacklisted tokens after log out
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)