import os

from flask import Flask, jsonify
from flask_restful import Api
from utils.utils import InvalidAPIUsage
from model.route_model import db
from flask_jwt_extended import JWTManager

from view.route_view import VistaPing, VistaRoutes, VistaRoute

# Initialize Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["JWT_SECRET_KEY"] = "users_s4cret_ke1"
#app.config['JWT_SECRET_KEY']='users_s4cret_ke1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
api.add_resource(VistaPing, "/routes/ping")
api.add_resource(VistaRoutes, "/routes/")
api.add_resource(VistaRoute, "/routes/<string:id_route>")


app_context = app.app_context();
app_context.push()
db.init_app(app)
db.create_all()
jwt = JWTManager(app)

@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002)