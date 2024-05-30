import requests
import os

class SAPSessionManager:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = os.getenv('SAP_B1_ENDPOINT')
        self.logged_in = False

    def login(self):
        if not self.logged_in:
            url = f"{self.base_url}/Login"
            data = {
                "UserName": os.getenv('SAP_B1_USERNAME'),
                "Password": os.getenv('SAP_B1_PASSWORD'),
                "CompanyDB": os.getenv('SAP_B1_COMPANYDB')
            }
            response = self.session.post(url, json=data)
            if response.status_code == 200:
                self.logged_in = True
                return True
            else:
                print("Failed to login:", response.text)
                return False
        return True

    def request(self, method, endpoint, **kwargs):
        if not self.logged_in:
            if not self.login():
                raise Exception("Unable to log in to SAP B1 Service Layer")
        
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, **kwargs)
        if response.status_code == 401:  # Unauthorized, login again
            self.logged_in = False
            if self.login():
                response = self.session.request(method, url, **kwargs)
        return response
