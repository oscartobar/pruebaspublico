from flask import Flask
from modelos.modelos import db
import requests
from flask_restful import Api
from flask import Flask, request
from flask_jwt_extended import JWTManager
import os

from view.vistas import VistaConsulta,VistaCreacion,VistaPing,VistaReset


def create_app(ambiente):
    
    app = Flask(__name__)
    
    if ambiente == 'PRODUCCION':
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        app_context = app.app_context()
        app_context.push()
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ofertas.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        app_context = app.app_context()
        app_context.push()
        
    api = Api(app)
    api.add_resource(VistaCreacion, '/offers')
    api.add_resource(VistaPing, '/offers/ping')
    api.add_resource(VistaReset, '/offers/reset')
    api.add_resource(VistaConsulta, '/offers/<offerid>')

    app_context = app.app_context()
    app_context.push()
    db.init_app(app)
    db.create_all()
    jwt = JWTManager(app)    
    
    return app   


