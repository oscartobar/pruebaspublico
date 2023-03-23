import requests
import os
from functools import wraps
import json
from flask import request

from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt_header
from flask_jwt_extended import get_jwt_header
from flask_jwt_extended.utils import decode_token



def validate_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = str(request.headers.get('Authorization'))
            #URL = os.environ['URLSEGURIDAD']
            URL = 'http://users:3000'
            headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
            }
            resp = requests.get(URL + "/users/me", headers=headers)
            if resp.status_code == 200:
                return fn(*args, **kwargs)
            else:
                return {"message":"El token no es válido o está vencido"}, resp.status_code
            
        return decorator

    return wrapper

class InvalidAPIUsage(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv