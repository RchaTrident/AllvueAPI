import os
import requests
import json

from utils import baseURL, authToken, clientId
print (authToken)
authToken2 = authToken["Authorization"]


def get_banks():
    url = 'https://api.prd.azure.us.allvuecloud.com/fund-accounting/v1/banks'
    params = {
        "Limit" : 1000,
        "Count" : True,
        "Code" : "MVP AS I"
    }
    headers = {
        'Allvue-Client-Id': 'tridenttrust',
        'Allvue-Fund-Acct-Company-Name': 'Trident Trust',
        # 'Allvue-Fund-Acct-Company-Name': 'Trident Trust Trn. 01Feb2022',
        'Authorization': f"Bearer {authToken2}",
        'accept': 'text/plain'
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"


banks_data = get_banks()
print(banks_data)

