import os
import requests
import json

from utils import baseURL, authToken, clientId

class AllvueParameters:
    def __init__(self, auth_token, client_id):
        self.base_url = 'https://api.prd.azure.us.allvuecloud.com'
        self.auth_token = auth_token["Authorization"]
        self.client_id = client_id
        self.headers = {
            'Allvue-Client-Id': self.client_id,
            'Authorization': f"Bearer {self.auth_token}",
            'accept': 'application/json'
        }

    def get_currencies(self, search):
        url = f'{self.base_url}/crm/v1/currencies'
        params = {
            "SearchText" : search
        }
        response =  requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_industries(self,search):
        url = f'{self.base_url}/crm/v1/industries'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_contacts(self,search):
        url = f'{self.base_url}/crm/v1/contacts'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_CAgreements(self,search):
        url = f'{self.base_url}/crm/v1/confidentiality-agreements'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_CGroups(self,search):
        url = f'{self.base_url}/crm/v1/company-groups'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_communication_types(self,search):
        url = f'{self.base_url}/crm/v1/communications/types'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_investor_groups(self,search):
        url = f'{self.base_url}/crm/v1/investor-groups'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def get_geography(self,search):
        url = f'{self.base_url}/crm/v1/geographies'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
  
api = AllvueParameters(authToken, 'tridenttrust') 

search_investorGroups = api.get_investor_groups(search="a")
search_industries = api.get_industries(search=None)
search_geography = api.get_geography(search=None)
search_currencies = api.get_currencies("U")

# print(search_currencies)
# print(search_investorGroups)
# print(search_industries)
# print(search_geography)


