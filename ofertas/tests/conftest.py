import os
import tempfile
import pytest


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

