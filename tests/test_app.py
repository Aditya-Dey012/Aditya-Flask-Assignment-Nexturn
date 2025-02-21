import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import app, db, User

@pytest.fixture
def client():
    """Set up a test client for Flask"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client  # Provide client for testing
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_user(client):
    """Test the user creation API"""
    response = client.post('/users', json={"name": "John", "email": "john@example.com"})
    assert response.status_code == 201  # Expecting HTTP 201 Created
    data = response.get_json()
    assert data['user']['name'] == "John"
    assert data['user']['email'] == "john@example.com"

def test_get_users(client):
    """Test retrieving all users"""
    client.post('/users', json={"name": "Alice", "email": "alice@example.com"})
    response = client.get('/users')
    assert response.status_code == 200  # Expecting HTTP 200 OK
    data = response.get_json()
    assert len(data) > 0  # At least one user should be present

def test_update_user(client):
    """Test updating user details"""
    client.post('/users', json={"name": "Bob", "email": "bob@example.com"})
    response = client.put('/users/1', json={"name": "Bobby"})
    assert response.status_code == 200  # Expecting HTTP 200 OK
    data = response.get_json()
    assert data['user']['name'] == "Bobby"

def test_delete_user(client):
    """Test deleting a user"""
    client.post('/users', json={"name": "Charlie", "email": "charlie@example.com"})
    response = client.delete('/users/1')
    assert response.status_code == 200  # Expecting HTTP 200 OK
    data = response.get_json()
    assert data['message'] == "User deleted!"
