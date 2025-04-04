import os
import requests
import json

from utils import baseURL, authToken, clientId

class AllvueFunds:
    def __init__(self, auth_token, client_id):
        self.base_url = 'https://api.prd.azure.us.allvuecloud.com'
        self.auth_token = auth_token["Authorization"]
        self.client_id = client_id
        self.headers = {
            'Allvue-Client-Id': self.client_id,
            'Authorization': f"Bearer {self.auth_token}",
            'accept': 'application/json'
        }

    def get_funds(self, search):
        url = f'{self.base_url}/crm/v1/funds'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def create_fund(self, name):
        url = f'{self.base_url}/crm/v1/funds'
        body = {
            "fundAccountingCode": "XYZ123RC",
            "submittedToFundAccounting": True,
            "clientFundAccountingCode": "FAC123",
            "name": name,
            "id": None,
            "type": 206320000,
            "fundCurrencyId": "0daeee05-95ea-e911-80dc-000d3a4558bd",
            "dateOfInception": "2023-01-01T00:00:00Z",
            "expectedTerminationDate": "2030-01-01T00:00:00Z",
            "carriedInterestPercentage": 10.00,
            "clawbackProvision": "Sample clawback provision",
            "investmentStrategy": "Buyout",
            "carryType": "DealbyDeal",
            "carryRate": 5,
            "carryRateComments": "Sample carry rate comments",
            "accountingBasis": "IFRS",
            "managementFeePercentage": 2.00,
            "mostRecentAuditDate": "2023-07-01T00:00:00Z",
            "auditorId": 'e92ac329-516c-4e02-ba91-efc10f346391',
            "auditorName": "Sample Auditor",
            "mostRecentLpaDate": "2023-07-01T00:00:00Z",
            "dateOfSideLetters": "2024-01-01T00:00:00Z",
            "legacyCode": "LEGACY01",
            "firmId": 'e92ac329-516c-4e02-ba91-efc10f346391',
        }
        
        response = requests.post(url, headers=self.headers, json=body)
        return self._handle_response(response)

        if 200 <= response.status_code <= 300:
            if response.text:  # Check if the response body is not empty
                return response.json()
            else:
                return "Success: No content returned"
        else:
            return f"Error: {response.status_code}, {response.text}"

api = AllvueFunds(authToken, 'tridenttrust')

created_fund = api.create_fund("RiverFund2")
search_fund = api.get_funds("river")

# print(created_fund)
# print(search_fund)
