import json
import jsonpath
import pytest
import logging
import logging.config

logging.config.fileConfig(fname='../logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@pytest.fixture
def read_file():
    try:
        with open('../test_data/current_price.json', "r") as file:
            return file.read()
    except:
        logger.error("file not readavle for currency prices from test_data")
    

@pytest.mark.e2e
def test_currency_code(read_file):
    json_obj = json.loads(read_file)
    json_path_list = jsonpath.jsonpath(json_obj, "chartName")
    logger.info("Checking chartname from bitcoin response")
    assert json_path_list[0] == "Bitcoin", "ChartName is not matched"
        




    



