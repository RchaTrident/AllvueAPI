import os
import requests
import json



clientId= "0oaimxpll5DMDySTQ5d7"
clientSecret = "DUMi0X06jlWPIs9BeQSR90T4NCTtSEx4eK4sXjGWlhtu12elOyAfY2d0Oi3il_gQ"

# LordOfCinders2023!
baseURL = "https://api.prd.azure.us.allvuecloud.com/fund-accounting"

def getToken():
    url = "/v1/oauth2/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": clientId,
        "client_secret": clientSecret
    }
    response = requests.post(url=f"{baseURL}{url}", headers=headers, data=data)
    # print(response.json())
    json_data = {}
    json_data["Authorization"] = response.json()['access_token']
    return json_data
    


authToken = getToken()


