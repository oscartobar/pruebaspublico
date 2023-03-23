from src.view.route_view import VistaPing
from src.model.route_model import Route
from src.main import app
import json
from uuid import uuid4
from datetime import datetime, timedelta
from httmock import HTTMock, all_requests

@all_requests
def mock_success_auth(url, request):
  return { 'status_code': 200 }

@all_requests
def mock_failed_auth(url, request):
  return { 'status_code': 401 }

class TestRoutes():

  def test_ping(self):
    with app.test_client() as test_client:
      with HTTMock(mock_success_auth):
        response = test_client.get(
          f'/routes/ping'
        )
        response_json = json.loads(response.data)
        assert response.status_code == 200
  
  def test_create_route(self):
    token = uuid4()
    with app.test_client() as test_client:
      with HTTMock(mock_success_auth):
        response = test_client.post(
          '/routes/', json={
            'sourceAirportCode': 'ABC',
            'sourceCountry': 'ESP',
            'destinyAirportCode': 'AEC',
            'destinyCountry': 'ARG',
            'bagCost': 120
          },
          headers={'Authorization': f'Bearer {token}'}
        )
        response_json = json.loads(response.data)
        assert response.status_code == 201
  
  def test_create_route_exist(self):
    token = uuid4()
    with app.test_client() as test_client:
      with HTTMock(mock_success_auth):
        response = test_client.post(
          '/routes/', json={
            'sourceAirportCode': 'ABC',
            'sourceCountry': 'ESP',
            'destinyAirportCode': 'AEC',
            'destinyCountry': 'ARG',
            'bagCost': 120
          },
          headers={'Authorization': f'Bearer {token}'}
        )
        response_json = json.loads(response.data)
        assert response.status_code == 412
    
  def test_create_route_invalid_token(self):
    with app.test_client() as test_client:
      with HTTMock(mock_failed_auth):
        response = test_client.post(
           '/routes/', json={
            'sourceAirportCode': 'ABC',
            'sourceCountry': 'ESP',
            'destinyAirportCode': 'AEC',
            'destinyCountry': 'ARG',
            'bagCost': 120
          },
          headers={
            'Authorization': f'Bearer Invalid'
          }
        )

        assert response.status_code == 401
  
  def test_create_route_without_token(self):
    with app.test_client() as test_client:
      with HTTMock(mock_failed_auth):
        response = test_client.post(
           '/routes/', json={
            'sourceAirportCode': 'ABC',
            'sourceCountry': 'ESP',
            'destinyAirportCode': 'AEC',
            'destinyCountry': 'ARG',
            'bagCost': 120
          }
        )

        assert response.status_code == 401
  
  def test_get_routes(self):
    with app.test_client() as test_client:
      with HTTMock(mock_success_auth):
        response = test_client.get(
          f'/routes/'
        )
        response_json = json.loads(response.data)
        assert response.status_code == 200
  
  def test_get_route(self):
    with app.test_client() as test_client:
      with HTTMock(mock_success_auth):
        response = test_client.get(
          f'/routes/1'
        )
        response_json = json.loads(response.data)
        assert response.status_code == 200