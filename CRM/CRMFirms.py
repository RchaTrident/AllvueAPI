import os
import requests
import json

from utils import baseURL, authToken, clientId

class AllvueFirms:
    def __init__(self, auth_token, client_id):
        self.base_url = 'https://api.prd.azure.us.allvuecloud.com'
        self.auth_token = auth_token["Authorization"]
        self.client_id = client_id
        self.headers = {
            'Allvue-Client-Id': self.client_id,
            'Authorization': f"Bearer {self.auth_token}",
            'accept': 'application/json'
        }

    def get_firm(self, search):
        url = f'{self.base_url}/crm/v1/firms'
        params = {
            "SearchText": search,
            "Limit": 20,
            "Count": True
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)
    
    def create_firm(self, name):
        url = f'{self.base_url}/crm/v1/firms'
        body = {
            "name": name,
            "fundAccountingCode": "AC1234",
            "submittedToFundAccounting": True,
            "businessDescription": "Second line address example.",
            "entityType": 315930002,
            "entityPrivateEquityType":937780007,
            "foreignInvestor": False,
            "investorType": 315930019,
            "calPersRegion": 861130010,
            "isInvesteeCompany": True,
            "isInvesteeFund": False,
            "isInvestor": False,
            "isVendor": False,
            "legacyCode": "LEGACYFIRM01",
            "legalName": "Sample Firm Legal Name",
            "erisa": True,
            "investorPrivateEquityClass": 937780000,
            "publicCompany": False,
            "shortBusinessDescription": "Brief business description.",
            "taxId": "TAX123456",
            "ticker": "TCKR",
            "investmentRoleType": 937780001,
            "externalId": "EXT123456",
            "investorSubtype": "Subtype A",
            "lastAppointmentDate": "2023-10-01T00:00:00Z",
            "preferredInvestmentTypes": [315930001, 315930002, 315930003],
            "preferredSectors": [315930000, 315930004, 315930008],
            "coInvestmentLimitAmount": 1000000.00,
        }
        response = requests.post(url, headers=self.headers, json=body)
        return self._handle_response(response)
    

api = AllvueFirms(authToken, 'tridenttrust')
created_firm = api.create_firm("RiverFirm2")
search_firm = api.get_firm("sample")

print(created_firm)
print(search_firm)