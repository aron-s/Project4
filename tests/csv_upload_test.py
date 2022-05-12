"""Testing csv uploads being created"""
import os

def test_uploads():
    """test uploads"""
    assert os.path.exists('./app/uploads/music.csv') == True

def test_database():
    """test database once csv is processed"""
    assert os.path.exists('./database/db2.sqlite') == True
