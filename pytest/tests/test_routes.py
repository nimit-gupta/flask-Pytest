import pytest
import json
import os,sys
#sys.path.append('/app')  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))

from app import app

@pytest.fixture(scope='module')

def test_client():

    with app.test_client() as pyClient:
 
        with app.app_context():
		
            yield pyClient 


def test_home_page(test_client):
    """Test the / route """
    response = test_client.get('/')
    assert response.mimetype == 'text/html'
    assert response.status_code == 200


def test_next_page(test_client):
    """Test /next route"""
    response = test_client.get('/next')
    assert response.mimetype == 'text/html'
    assert response.status_code == 200
    
'''
#route doesn't exists, so in functional test it will fail
def test_back_page(test_client):
    """Test back"""
    response = test_client.get('/back')
    assert response.mimetype == 'text/html'
    assert response.status_code == 200
'''

def test_data_page(test_client):
    data =      {
                  "fname" : "nimit",
                  "lname" : "gupta"
                }

    response = test_client.post('/data', data = json.dumps(data), content_type='application/json')

    assert response.mimetype == "application/json"
    assert response.status_code == 200
    #assert response.json[data["fname"]] == "nimit"