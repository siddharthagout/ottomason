import requests
from configparser import ConfigParser
import json

import os
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.cfg')
config = ConfigParser()
data = config.read(initfile)
def get_response():
    print(data)
    page = config.get('page_numbers', 'page')
    print("page no : ", page)
    url = "https://reqres.in/api/users?page={}".format(page)
    response = requests.get(url)
    json_obj = response.json()
    # print(json_obj)
    url = json.loads(response.headers["Report-To"])["endpoints"][0]["url"]


    print(url)
    

    # try:
    #     page = json_obj['page']
    #     print("we are on page no {}.".format(page))
       
    # except KeyError:
    #     page = json_obj['pages']
    #     print("{} page no is not found".format(KeyError))

    # finally:
    #     print("This is finally block code")


if __name__ == "__main__":
    get_response()
