import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Route(db.Model):
    __tablename__ = 'route'
    id = db.Column(db.Integer, primary_key=True)
    sourceAirportCode = db.Column(db.String(3), nullable=False)
    sourceCountry = db.Column(db.String(100))
    destinyAirportCode = db.Column(db.String(3), nullable=False)
    destinyCountry = db.Column(db.String(100))
    bagCost = db.Column(db.Float, default= 0)
    createdAt = db.Column(db.DateTime)

class RouteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Route
        load_instance = True