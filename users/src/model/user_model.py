import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.LargeBinary)
    salt = db.Column(db.LargeBinary)
    token = db.Column(db.String(500))
    expireAt = db.Column(DateTime(timezone=True))
    createdAt = db.Column(DateTime(timezone=True), server_default=func.now())

