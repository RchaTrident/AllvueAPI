import os
import requests
import json

from utils import baseURL, authToken, clientId
print (authToken)
authToken2 = authToken["Authorization"]


def get_journal():
    # url = 'https://api.prd.azure.us.allvuecloud.com/fund-accounting/v1/general-journals/{journalTemplateName}/{journalBatchName}/lines'
    url = 'https://api.prd.azure.us.allvuecloud.com/fund-accounting/v1/general-journals/general/BAMAF QP/lines'
    params = {
        "Limit" : 1000,
        "Count" : True
    }
    headers = {
        'Allvue-Client-Id': 'tridenttrust',
        'Allvue-Fund-Acct-Company-Name': 'Trident Trust',
        'Authorization': f"Bearer {authToken2}",
        'accept': 'text/plain'
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
journal_data = get_journal()
print(journal_data)
