from app import db
from datetime import datetime


class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=True)
    short = db.Column(db.String(255), unique=True, nullable=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())


# class AdminModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(140))
#     last_name = db.Column(db.String(140))
#     username = db.Column(db.String(140), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)