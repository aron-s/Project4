"""Testing csv uploads being created"""
import os

def test_uploads():
    """test uploads"""
    assert os.path.exists('./app/uploads/') == True

def test_database():
    """test database once csv is processed"""
    assert os.path.exists('./database/') == True
