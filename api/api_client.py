from requests import Session
from api.endpoints import *

class APIClient:

    def __init__(self):
        self.base_url = PEOPLE_BASE_URL
        self.session = Session()

    
    def get(self, endpoint, headers=None, params=None, timeout=None):
        url = self.base_url + endpoint
        response = self.session.get(url, headers=headers, params=params, timeout=timeout)
        return response
    

    def post(self, endpoint, headers=None, json=None, timeout=None):
        url = self.base_url + endpoint
        response = self.session.post(url, headers=headers, json=json, timeout=timeout)
        return response


    def put(self, endpoint, headers=None, json=None, timeout=None):
        url = self.base_url + endpoint
        response = self.session.put(url, headers=headers, json=json, timeout=timeout)
        return response


    def detele(self, endpoint, headers=None, json=None, timeout=None):
        url = self.base_url + endpoint
        response = self.session.delete(url, headers=headers, json=json, timeout=timeout)
        return response