import requests
import json
import pytest
import random
from api.endpoints import *
from datetime import datetime


@pytest.fixture
def get_request_data():
    with open("../test_data/create_activity_payload.json", "r") as payload:
        json_obj = json.loads(payload.read())
        json_obj["title"] = random.choice(["sid","rahul","naresh","mini","aaru","mom","dad"])
        json_obj["dueDate"] = datetime.utcnow().isoformat()[:-3]+'Z'
        json_obj["id"] = random.randint(0, 1000)
        # print(json_obj)
        return json_obj
    
def set_headers():
    headers = {
        "Content-Type": "application/*+json",
        "Accept":"application/json"
    }
    return headers

@pytest.fixture
def get_api_response(get_request_data):
    data = get_request_data
    response = requests.post(BASE_URL+ACTIVITY, 
                            json=data, 
                            headers=set_headers())
    return response

@pytest.mark.sanity
@pytest.mark.e2e    
def test_verify_success_status_code(get_api_response):
    response = get_api_response    
    assert response.status_code == 200, "http status code not matched"
    
@pytest.mark.regression
@pytest.mark.e2e
def test_verify_completed_status(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    assert json_obj["completed"] == True, "completed status did not match"
