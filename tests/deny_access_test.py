"""
Test for denying and approving access to dashboard and csv file.
"""

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
