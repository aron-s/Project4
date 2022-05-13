"""
Test for transactions.
"""

def test_transac_access(client):
    """Test for access to uploading file"""
    with client:
        client.post('/login', data=dict(email='test@njit.edu', password='testtest'))
        res = client.get('/transactions', follow_redirects=True)
        assert res.status_code == 200
        assert b"Transactions" in res.data

def calc_transaction_balance(client):
    """Test for calculating balance"""
    with client:
        client.post('/login', data=dict(email='test@njit.edu', password='testtest'))
        res = client.get('/transactions', follow_redirects=True)
        assert res.status_code == 200
        assert b"Total balance" in res.data

