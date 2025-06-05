# main.py

from scanner import SQLiScanner
from report import generate_report
import argparse
import urllib.parse

def parse_query_string(query):
    params = urllib.parse.parse_qs(query)
    # parse_qs returns values as lists, convert to single values for simplicity
    return {k: v[0] for k, v in params.items()}

def main():
    parser = argparse.ArgumentParser(description="SQL Injection Detection Tool")
    parser.add_argument("url", help="Target URL (include query parameters for GET)")
    parser.add_argument("-X", "--method", choices=['GET', 'POST'], default='GET', help="HTTP method to use")
    parser.add_argument("-d", "--data", help="POST data in key=value&key2=value2 format (for POST method)")
    args = parser.parse_args()

    url = args.url
    method = args.method.upper()

    if method == 'GET':
        parsed_url = urllib.parse.urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        params = parse_query_string(parsed_url.query)
        data = None
    else:
        base_url = url
        params = None
        data = parse_query_string(args.data) if args.data else {}

    scanner = SQLiScanner(base_url, method, params, data)
    scanner.scan()
    vulnerabilities = scanner.get_report()
    generate_report(vulnerabilities)

if __name__ == "__main__":
    main()
