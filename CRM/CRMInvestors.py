import os
import requests
import json

from utils import baseURL, authToken, clientId


class AllvueInvestors:
    def __init__(self, auth_token, client_id):
        self.base_url = 'https://api.prd.azure.us.allvuecloud.com'
        self.auth_token = auth_token["Authorization"]
        self.client_id = client_id
        self.headers = {
            'Allvue-Client-Id': self.client_id,
            'Authorization': f"Bearer {self.auth_token}",
            'accept': 'application/json'
        }

    def get_investors(self, search):
        url = f'{self.base_url}/crm/v1/company-investors'
        params = {
            "SearchText": search,
            "Limit": 50,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def create_investor(self, name, fund_id, firm_id, fa=True):
        url = f'{self.base_url}/crm/v1/company-investors'
        body = {
            "name": name,
            "fundId": fund_id,
            "firmId": firm_id,
            "FA": fa,
            "submittedToFundAccounting": True,
            "commitment": 9000000000,
            "shortName" : "RiverLegacy",
            "transactionCurrencyId" : "0daeee05-95ea-e911-80dc-000d3a4558bd"
        }

        response = requests.post(url, headers=self.headers, json=body)
        return self._handle_response(response)

    def update_investor(self, id, name, fund_id, firm_id):
        url = f'{self.base_url}/crm/v1/company-investors/{id}'
        body = {
            "name": name,
            "fundId": fund_id,
            "firmId": firm_id,
            "FA": True,
            "submittedToFundAccounting": True,
            # "fundAccountingCode": fund_accounting_code,
            # "commitment": commitment,
            "statusReason": "active",
            "shortName" : "RiverLegacy",
            # "inactive" : False,
            "transactionCurrencyId" : "0daeee05-95ea-e911-80dc-000d3a4558bd",
            # "status" : 0,
            # "includeInPortal": True

            
        }
        response = requests.put(url, headers=self.headers, json=body)
        return self._handle_response(response)

    def activate_investor(self, id):
        url = f'{self.base_url}/crm/v1/company-investors/{id}/activate'
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def delete_investor(self, id):
        url = f'{self.base_url}/crm/v1/company-investors/{id}'
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)

api = AllvueInvestors(authToken, 'tridenttrust')
search_investors = api.get_investors("river")
created_investor = api.create_investor("RiverInvestor", '28cb0ad6-d7ba-4fc6-8e27-860efcf8a03e', "e92ac329-516c-4e02-ba91-efc10f346391")
updated_investor = api.update_investor("dfad3688-b280-4551-8fb5-5e25d7a5785f", "RiverInvestorUpdated", '28cb0ad6-d7ba-4fc6-8e27-860efcf8a03e', "e92ac329-516c-4e02-ba91-efc10f346391")
deleted_investor = api.delete_investor('9faa8f9c-d06e-4b07-a4f8-c3de0d1a6674')

print(deleted_investor)
print(search_investors)
print(updated_investor)
print(created_investor)