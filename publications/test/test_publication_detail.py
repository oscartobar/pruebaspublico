from src.vistas.vistas import PublicationDetail

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

class TestPublicationDetail(unittest.TestCase):

    def test_publication_detail_with_valid_id(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context():
                    id_post = 1
                    publication_detail = PublicationDetail().get(id_post)
                    self.assertEqual(publication_detail[1], 200)


    def test_publication_detail_with_invalid_id(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context():
                    id_post = 'abc'
                    publication_detail = PublicationDetail().get(id_post)
                    self.assertEqual(publication_detail[1], 400)

    def test_publication_detail_with_not_exist_id(self):
        with HTTMock(mock_success_auth):
            with patch('src.vistas.utils.validateToken') as mock_get_orgs:
                mock_get_orgs.return_value = 200
                mock_get_orgs.return_value = [{
                    "data": {"id": "1", "username": "test", "email": "test@test"}
                }]
                with app.test_request_context():
                    id_post = 584
                    publication_detail = PublicationDetail().get(id_post)
                    self.assertEqual(publication_detail[1], 404)

"""
    def test_publicaction_detail_invalid_token(self):
        with app.test_request_context():
            id_post = 584
            publication_detail = PublicationDetail().get(id_post)
            self.assertEqual(publication_detail[1], 404)
"""
