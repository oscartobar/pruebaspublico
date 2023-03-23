from flask import Flask
from modelos.modelos import db
import requests
from flask_restful import Api
from flask import Flask, request
from flask_jwt_extended import JWTManager
from utils.pruebas import create_app
from view.vistas import VistaConsulta,VistaCreacion,VistaPing,VistaReset

app = create_app("PRODUCCION")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3003)

