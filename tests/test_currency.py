import json
import jsonpath
import pytest

@pytest.fixture
def read_file():
    with open('../test_data/current_price.json', "r") as file:
        return file.read()
    

@pytest.mark.e2e
def test_currency_code(read_file):
    json_obj = json.loads(read_file)
    json_path_list = jsonpath.jsonpath(json_obj, "chartName")
    assert json_path_list[0] == "Bitcoin", "ChartName is not matched"
        




    



