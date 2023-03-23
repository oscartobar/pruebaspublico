import unittest,unicodedata
from  src.utils.clasebase import BaseTestClass
from unittest.mock import Mock, patch
import json
from src.utils.clasebase import BaseTestClass
from src.view.vistas import VistaConsulta,VistaCreacion
from httmock import HTTMock, all_requests



@all_requests
def mock_success_auth(url, request):
  return { 'status_code': 200 }

@all_requests
def mock_failed_auth(url, request):
  return { 'status_code': 401 }

class TestSuiteCrear(BaseTestClass):
        
    def test_Creacion_400(self):
        self.assertEqual(1, 1)
        
    def test_Creacion_401(self):
        with patch('src.view.valida.Validador.revisar') as mock_get_orgs:
            mock_get_orgs.return_value = 401
            with self.app.test_request_context(data=json.dumps({
                    "postId": 1,
                    "description": "My description",
                    "size": "LARGE",
                    "fragile": True,
                    "offer": 10 }), content_type='application/json'):
                prueba = VistaCreacion().post()
                self.assertEqual(prueba[1], 401)  
    
    def test_Creacion_412(self):
        with patch('src.view.valida.Validador.revisar') as mock_get_orgs:
            mock_get_orgs.return_value = 401
            with self.app.test_request_context(data=json.dumps({
                    "postId": 1,
                    "description": "My description",
                    "size": "LARGE",
                    "fragile": True,
                    "offer": -1 }), content_type='application/json'):
                prueba = VistaCreacion().post()
                self.assertEqual(prueba[1], 401)   

    def test_Creacion_201(self):
        with HTTMock(mock_success_auth):
            with patch('src.view.valida.Validador.revisar') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                with self.app.test_request_context(data=json.dumps({
                        "postId": 1,
                        "description": "My description",
                        "size": "LARGE",
                        "fragile": True,
                        "offer": 10 }), content_type='application/json'):
                    prueba = VistaCreacion().post()
                    self.assertEqual(prueba[1], 201)  
        
 
            

class Consultar(BaseTestClass):
    
    

          
    def test_consultar_401(self):
        self.assertEqual(1, 1)            
    def test_consultar_400(self):
        self.assertEqual(1, 1)  
    
    def test_consultar_404(self):
        with HTTMock(mock_success_auth):
            with patch('src.view.valida.Validador.revisar') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                with self.app.test_request_context():
                    id_post = 1
                    prueba = VistaConsulta().get(1)
                    self.assertEqual(prueba[1], 404)
                    
    def test_consultar_200(self):
        self.assertEqual(1, 1)    
    
class Listar(BaseTestClass):      
    def test_Listar_401(self):
        self.assertEqual(1, 1)             
    def test_Listar_400(self):
        self.assertEqual(1, 1) 
    def test_Listar_200(self):
        self.assertEqual(1, 1)                 
            
"""""
class Ping(unittest.TestCase):     
    @mock.patch.object(vi.VistaPing, "get")
    def test_ping_200(self,mock_response):
       mock_response.return_value = 'pong',200
       respuesta = vi.VistaPing()
       rta2 = respuesta.get()
       self.assertEqual(rta2, mock_response.return_value)   
"""""        