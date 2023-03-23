from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from modelos.modelos import db
from vistas.vistas import Ping, CreatePublication, PublicationsList, PublicationDetail

import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()

#db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(Ping, "/posts/ping")
api.add_resource(CreatePublication, "/posts")
api.add_resource(PublicationsList, "/posts")
api.add_resource(PublicationDetail, "/posts/<string:id_post>")
jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)








