from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routeId = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    plannedStartDate = db.Column(db.DateTime, nullable=False)
    plannedEndDate = db.Column(db.DateTime, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Publication('{self.id}', '{self.routeId}', '{self.userId}', '{self.plannedStartDate}', '{self.plannedEndDate}', '{self.createdAt}')"
