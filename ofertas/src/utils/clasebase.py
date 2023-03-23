import unittest
import requests
import os
from src.utils.pruebas import db,create_app
from uuid import uuid4
from datetime import datetime, timedelta
from httmock import HTTMock, all_requests

class BaseTestClass(unittest.TestCase):
   
    def setUp(self):
        self.app = create_app("PRUEBAS")
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()
            #mitoken = create_user()
            
    @staticmethod
    def create_user_mock(self):
        URL = os.environ['URLSEGURIDAD']
        data = {"username": "test", "password": "test", "email": "test@test.com"}
        mitoken = requests.get(URL + "/users/", json=data)
        return mitoken.status_code
        
        
    def tearDown(self):
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()