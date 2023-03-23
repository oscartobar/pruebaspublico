from datetime import datetime

from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, verify_jwt_in_request
from flask_restful import Resource

from model.user_model import User, db
from utils.utils import hash_new_password, get_datetime_iso_format, is_correct_password, get_expiration_datetime


class VistaPing(Resource):
    def get(self):
        return "Pong"


class VistaSignUp(Resource):
    def post(self):
        try:
            username = request.json["username"]
            email = request.json["email"]
            password = request.json["password"]
        except:
            return "", 400
        if username is None or email is None or password is None:
            return "", 400

        usuario_username = User.query.filter(User.username == request.json["username"]).first()
        usuario_email = User.query.filter(User.email == request.json["email"]).first()
        if usuario_username is not None or usuario_email is not None:
            return "", 412
        salt, pw_hash = hash_new_password(password)
        today = datetime.now()
        created_date = get_datetime_iso_format(today)
        new_user = User(email=email, username=username, password=pw_hash, salt=salt, createdAt=today)
        token = create_access_token(identity=new_user.id)
        new_user.token = token
        db.session.add(new_user)
        db.session.commit()
        return {
                   "id": new_user.id,
                   "createdAt": created_date
               }, 201


class VistaLogIn(Resource):
    def post(self):
        try:
            username = request.json["username"]
            password = request.json["password"]
        except:
            return "", 400
        if username is None or password is None:
            return "", 400
        usuario = User.query.filter(User.username == username).first()
        if usuario is not None:
            salt = usuario.salt
            pw_hash = usuario.password
            if is_correct_password(salt, pw_hash, password):
                token = create_access_token(identity=usuario.id)
                expiration_date = get_expiration_datetime()
                return {"id": usuario.id, "token": token, "expireAt": expiration_date}, 200
            else:
                return "", 422
        else:
            return "", 404


class VistaUserInfo(Resource):
    def get(self):
        try:
            verify_jwt_in_request(optional=True)
        except:
            return "", 401
        jwt_header = get_jwt()
        if jwt_header == {}:
            return "", 400
        id_usuario = get_jwt_identity()
        if id_usuario is None:
            return "", 401
        usuario = User.query.filter(User.id == id_usuario).first()
        return {"id": id_usuario, "username": usuario.username, "email": usuario.email}, 200
