import requests
import pandas as pd
import numpy as np
import datetime as dt

class ThetaDataAPI:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:25510/'

    def _get_req(self, url: str, headers: dict, params: dict=None):
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)

    def get_roots(self, security_type: str='OPTION'):
        url = f'{self.base_url}list/roots?sec={security_type}'
        headers = {'Accept': 'application/json'}
        return self._get_req(url=url, headers=headers)

    def get_expirations(self, root:str):
        url = f'{self.base_url}list/expirations?root={root}'
        headers = {'Accept': 'application/json'}
        return self._get_req(url=url, headers=headers)
    
    def get_strikes(self, root: str, exp: str):
        url = f'{self.base_url}list/strikes?root={root}&exp={exp}'
        headers = {'Accept': 'application/json'}
        return self._get_req(url=url, headers=headers)
    
    def get_dates(self, root: str, security_type: str="option", exp: str=None, strike_right: tuple[str, str]=None):
        url = f'{self.base_url}list/dates/{security_type}/quote'
        url_params = {}
        url_params["root"] = root
        if exp is not None:
            url_params["exp"] = exp
        if strike_right is not None:
            url_params["strike"] = strike_right[0]
            url_params["right"] = strike_right[1]
        headers = {'Accept': 'application/json'}
        return self._get_req(url=url, headers=headers, params=url_params)   

    
if __name__ == "__main__":
    client = ThetaDataAPI()
    root = "AAPL"
    expiries = client.get_expirations(root=root)["response"]
    exp = expiries[len(expiries)-50]
    print(expiries)
    strikes = client.get_strikes(root=root, exp=exp)
    print(strikes)
    dates = client.get_dates(root=root, exp=exp)
    print(dates)