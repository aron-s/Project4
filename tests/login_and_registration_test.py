"""
Test for logging in and registration and authorization
"""
import logging

from app import db
from app.db.models import User, Song

# def test_index_page_not_logged_in(client):
#     res = client.get('./dashboard')
#     assert res.status_code == 401

def test_profile_page_logged_in(client):
    """Test for login"""
    with client:
        client.post('/login', data=dict(email='test@njit.edu', password='testtest'))
        res = client.get('/profile')
        assert res.status_code == 200
        assert b"About" in res.data

def test_user_registration(client):
    """Test for registration"""
    with client:
        res = client.post('/register', data=dict(email='register@njit.edu', password='testtest', confirm='testtest'), follow_redirects=True)
        assert res.status_code == 200
        assert b"Congratulations, you are now a registered user!" in res.data

def test_access_dashboard(client):
    """Test for accessing dashboard as logged in user"""
    with client:
        client.post('/login', data=dict(email='test@njit.edu', password='testtest'))
        res = client.get('/dashboard', follow_redirects=True)
        assert res.status_code == 200
        assert b"Welcome" in res.data

def test_deny_dashboard_access(client):
    """Test for denying dashboard access"""
    with client:
        res = client.get('/dashboard', follow_redirects=True)
        assert b"Please log in to access this page." in res.data
        assert res.status_code == 200


def test_deny_csv_upload(client):
    """Test for denying access to uploading csv file"""
    with client:
        res = client.get('/songs/upload', follow_redirects=True)
        assert b"Please log in to access this page." in res.data
        assert res.status_code == 200




