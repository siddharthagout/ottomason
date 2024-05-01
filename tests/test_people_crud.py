from api.api_client import APIClient
from api import endpoints
import pytest
import json
from utils import user_ops
import logging
import logging.config

logging.config.fileConfig(fname='../logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


apc = APIClient()

@pytest.fixture(scope="module")
def get_api_response():
    logger.info("Hitting GET people API for fetching the response")
    url = endpoints.PEOPLE_ENDPOINT
    response = apc.get(url)
    return response

@pytest.fixture(scope="module")
def create_people_request():
    user = user_ops.generate_random_name()

    try:
        with open("../test_data/people.json", "r") as people:
            json_obj = json.loads(people.read())
        
        
        json_obj['fname'] = user[0]
        json_obj['lname'] = user[1]
        logger.info("setting user first and last name as {} {}".format(json_obj['fname'],json_obj['lname']))

        return json_obj
    except:
        logger.error("People request json missing from location")


@pytest.fixture(scope="module")
def create_poeople(create_people_request):
    logger.info("Hitting create people API")
    url = endpoints.PEOPLE_ENDPOINT
    response = apc.post(url, json=create_people_request)
    return response

@pytest.fixture(scope="module")
def start_stop():
    logger.info("started executing the testcases")
    yield
    logger.info("finished executing the testcases.")



@pytest.mark.people_sanity
def test_people_api_status_code(get_api_response,start_stop):
    response = get_api_response
    assert response.status_code == 200, "HTTP status not matched"


@pytest.mark.people_sanity
def test_people_api_people_count(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    assert len(json_obj) >= 3, "Get response object count for number of people not matched"

@pytest.mark.people_sanity
def test_people_api_check_specific_user_firstname(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    user_list = []
    for user in json_obj:
        user_list.append(user["fname"])
    assert "Tooth" in user_list, "User firstname not found in user list"


@pytest.mark.people_sanity
def test_people_api_check_specific_user_lastname(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    user_list = []
    for user in json_obj:
        user_list.append(user["lname"])
    assert "Fairy" in user_list, "User lastname not found in user list"

@pytest.mark.people_sanity
def test_people_api_check_timestamp(get_api_response):
    response = get_api_response
    json_obj = json.loads(response.text)
    timestamp_list = []
    for time in json_obj:
        timestamp_list.append(time["timestamp"])
    assert len(timestamp_list) >= 3, "Expected timestamp count 3 is not matched"

@pytest.mark.create_people_sanity
def test_create_people_status_code(create_poeople,start_stop):
    response = create_poeople
    logger.info("checking http status code for create people API response")
    assert response.status_code == 200, "HTTP status code 201 not matched"