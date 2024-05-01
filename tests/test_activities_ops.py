import requests
import json
import pytest
import random
from api.endpoints import *
from datetime import datetime
import logging
import logging.config

logging.config.fileConfig(fname='../logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@pytest.fixture
def get_request_data():
    try:
        logger.info("reading create_activity_payload.json payload data")
        with open("../test_data/create_activity_payload.json", "r") as payload:
            json_obj = json.loads(payload.read())
            json_obj["title"] = random.choice(["Sam","John", "Dakota", "Micheal", "Nicolas"])
            json_obj["dueDate"] = datetime.utcnow().isoformat()[:-3]+'Z'
            json_obj["id"] = random.randint(0, 1000)
            # print(json_obj)
            return json_obj
    except:
        logger.error("file not readable from test data for create activity payload")
    
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
    logger.info("checking status code for activity success")  
    assert response.status_code == 200, "http status code not matched"
    
@pytest.mark.regression
@pytest.mark.e2e
def test_verify_completed_status(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    logger.info("checking activity status as completed or not")
    assert json_obj["completed"] == True, "completed status did not match"
