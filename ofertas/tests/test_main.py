from unittest.mock import patch
import json
from src.utils.clasebase import BaseTestClass
from src.view.vistas import VistaPing,VistaReset,Validador
from httmock import all_requests, response, HTTMock
import requests
from src.main import app

@all_requests
def mock_success_auth(url, request):
  return { 'status_code': 200 }

@all_requests
def mock_failed_auth(url, request):
  return { 'status_code': 401 }

@all_requests
def response_content(url, request):
    headers = {'content-type': 'application/json',
            'Set-Cookie': 'foo=bar;'}
    content = {'message': 'API rate limit exceeded'}
    return response(403, content, headers, None, 5, request)
class test_VistaPing(BaseTestClass):
          
    def test_ping(self):     
        with self.app.test_request_context(data=json.dumps({
                  }), content_type='application/json'):
          prueba = VistaPing().get()
          self.assertEqual(prueba[1], 200)
    
    def test_reset(self):     
        with self.app.test_request_context(data=json.dumps({
                  }), content_type='application/json'):
          prueba = VistaReset().post()
          self.assertEqual(prueba[1], 200)      

    def test_main(self):     
        with self.app.test_request_context():
          miapp = app
          self.assertEqual( miapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] , self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
          
   

    def test_valida(self): 
        
        with HTTMock(response_content):
            r = requests.get('http://domain.com/')
            prueba = Validador().revisar(r)
            self.assertEqual(prueba, 401)  
            
    def test_valida_post(self): 
        with HTTMock(response_content):
            r = requests.post('http://domain.com/')
            prueba = Validador().revisar(r)
            self.assertEqual(prueba, 401)                            
                            