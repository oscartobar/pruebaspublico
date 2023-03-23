from src.vistas.vistas import PublicationsList

import unittest.mock
import unittest
from src.app import app
from unittest.mock import Mock, patch
from httmock import HTTMock, all_requests

@all_requests
def mock_success_auth(url, request):
  return { 'status_code': 200 }

@all_requests
def mock_failed_auth(url, request):
  return { 'status_code': 401 }

class TestPublicationsList(unittest.TestCase):

    def test_publication_list_without_params(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context():
                    publication_list = PublicationsList().get()
                    self.assertEqual(publication_list[1], 200)

    def test_publication_list_with_invalid_when(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(query_string={"when": "abc"}):
                    publication_list = PublicationsList().get()
                    self.assertEqual(publication_list[1], 400)

    def test_publication_list_with_invalid_route(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context(query_string={"route": "abc"}):
                    publication_list = PublicationsList().get()
                    self.assertEqual(publication_list[1], 400)

"""
    def test_publicaction_list_invalid_token(self):
        with app.test_request_context():
            id_post = 584
            publication_list = PublicationsList().get(id_post)
            self.assertEqual(publication_list[1], 404)
"""
