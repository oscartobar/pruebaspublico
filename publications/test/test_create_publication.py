from src.vistas.vistas import CreatePublication

import unittest.mock
import unittest
import json
from src.app import app
from unittest.mock import Mock, patch
from httmock import HTTMock, all_requests

@all_requests
def mock_success_auth(url, request):
  return { 'status_code': 200 }

@all_requests
def mock_failed_auth(url, request):
  return { 'status_code': 401 }

class TestCreatePublication(unittest.TestCase):

    def test_publication_create_with_valid_data(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(data=json.dumps({
                        "routeId": 1,
                        "plannedStartDate": "2023-12-25",
                        "plannedEndDate": "2023-12-30"
                    }), content_type='application/json'):
                    publication = CreatePublication().post()
                    self.assertEqual(publication[1], 201)

    def test_publication_create_with_incorrect_dates(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(data=json.dumps({
                        "routeId": 1,
                        "plannedStartDate": "2022-12-25",
                        "plannedEndDate": "2022-12-30"
                    }), content_type='application/json'):
                    publication = CreatePublication().post()
                    self.assertEqual(publication[1], 412)

    def test_publication_create_without_start_date(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(data=json.dumps({
                        "routeId": 1,
                        "plannedStartDate": "",
                        "plannedEndDate": "2023-12-30"
                    }), content_type='application/json'):
                    publication = CreatePublication().post()
                    self.assertEqual(publication[1], 400)

    def test_publication_create_without_end_date(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(data=json.dumps({
                        "routeId": 1,
                        "plannedStartDate": "2023-12-25",
                        "plannedEndDate": ""
                    }), content_type='application/json'):
                    publication = CreatePublication().post()
                    self.assertEqual(publication[1], 400)

    def test_publication_create_without_route(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(data=json.dumps({
                        "routeId": "",
                        "plannedStartDate": "2023-12-25",
                        "plannedEndDate": "2023-12-30"
                    }), content_type='application/json'):
                    publication = CreatePublication().post()
                    self.assertEqual(publication[1], 400)

"""
    def test_publicaction_detail_invalid_token(self):
        with app.test_request_context():
            id_post = 584
            publication = CreatePublication().post(id_post)
            self.assertEqual(publication[1], 404)
"""
