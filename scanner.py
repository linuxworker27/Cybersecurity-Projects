# scanner.py

from payloads import payloads
from request_handler import RequestHandler
from response_analyzer import analyze_response

class SQLiScanner:
    def __init__(self, url, method='GET', params=None, data=None, headers=None):
        self.url = url
        self.method = method.upper()
        self.params = params or {}
        self.data = data or {}
        self.headers = headers or {}
        self.vulnerabilities = []

    def scan(self):
        # Determine parameters to test based on method
        test_params = self.params if self.method == 'GET' else self.data
        if not test_params:
            print("No parameters to test.")
            return

        print(f"Starting scan on {self.url} using {self.method} method...")
        for param in test_params.keys():
            print(f"Testing parameter: {param}")
            for payload in payloads:
                handler = RequestHandler(self.url, self.method, self.params, self.data, self.headers)
                response = handler.send_request(param, payload)
                vulnerable, reason = analyze_response(response)
                if vulnerable:
                    self.vulnerabilities.append({
                        'parameter': param,
                        'payload': payload,
                        'reason': reason,
                        'url': response.url if response else self.url
                    })
                    print(f"[!] Vulnerability found on parameter '{param}' with payload '{payload}'")
                    # Stop testing this parameter after first vulnerability found
                    break
        print("Scan completed.")

    def get_report(self):
        return self.vulnerabilities
