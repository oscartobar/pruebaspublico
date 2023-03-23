from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import DateTime, func
import json
from json import JSONEncoder
import enum

db = SQLAlchemy()

class Oferta(db.Model):
    __tablename__ = 'ofertas'
    id = db.Column(db.Integer, primary_key = True)
    postId = db.Column(db.String(128))
    userId  =  db.Column(db.String(100))
    description =  db.Column(db.String(100))
    size = db.Column(db.String(100))
    fragile  = db.Column( db.Boolean(), nullable=True  )
    offer  =  db.Column(db.Float, default= 0)
    createdAt  =  db.Column(DateTime(timezone=True), server_default=func.now()                            )
    


class OfertaSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Oferta
         load_instance = True

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}