# request_handler.py

import requests

class RequestHandler:
    def __init__(self, url, method='GET', params=None, data=None, headers=None):
        self.url = url
        self.method = method.upper()
        self.params = params or {}
        self.data = data or {}
        self.headers = headers or {}

    def send_request(self, injection_param, payload):
        # Inject payload into the specified parameter
        if self.method == 'GET':
            test_params = self.params.copy()
            test_params[injection_param] = payload
            try:
                response = requests.get(self.url, params=test_params, headers=self.headers, timeout=10)
                return response
            except requests.RequestException as e:
                print(f"Request error: {e}")
                return None
        elif self.method == 'POST':
            test_data = self.data.copy()
            test_data[injection_param] = payload
            try:
                response = requests.post(self.url, data=test_data, headers=self.headers, timeout=10)
                return response
            except requests.RequestException as e:
                print(f"Request error: {e}")
                return None
        else:
            print(f"Unsupported HTTP method: {self.method}")
            return None
