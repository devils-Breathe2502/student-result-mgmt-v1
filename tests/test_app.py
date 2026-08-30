import pytest
from app import app, calculate_result

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_calculate_result_grade_a_plus():
    total, percentage, grade = calculate_result(95, 92, 96)
    assert total == 283
    assert grade == "A+"

def test_calculate_result_grade_f():
    total, percentage, grade = calculate_result(20, 15, 10)
    assert grade == "F"

def test_submit_result(client):
    response = client.post('/submit', data={
        'name': 'Test Student',
        'roll_no': '101',
        'marks1': '80',
        'marks2': '75',
        'marks3': '90'
    })
    assert response.status_code == 200
    assert b'Test Student' in response.data
