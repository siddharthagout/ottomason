import requests
from configparser import ConfigParser
import json
import os
import logging
import logging.config

logging.config.fileConfig(fname='../logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.cfg')
config = ConfigParser()
data = config.read(initfile)


def test_get_response():
    page = config.get('page_numbers', 'page')
    url = "https://reqres.in/api/users?page={}".format(page)
    response = requests.get(url)
    json_obj = response.json()
    url = json.loads(response.headers["Report-To"])["endpoints"][0]["url"]
    logger.info("checking URL from headers")
    assert url == "", "Valid url is fetched from headers"
    

    # try:
    #     page = json_obj['page']
    #     print("we are on page no {}.".format(page))
       
    # except KeyError:
    #     page = json_obj['pages']
    #     print("{} page no is not found".format(KeyError))

    # finally:
    #     print("This is finally block code")
