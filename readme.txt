# SQL Injection Detection Tool

This is a Python-based SQL Injection detection tool designed to help identify SQL injection vulnerabilities in web applications. It supports both GET and POST HTTP methods and uses common SQL injection payloads to test input parameters.

## Features

- Supports GET and POST requests.
- Tests multiple parameters with a curated list of SQL injection payloads.
- Detects SQL injection vulnerabilities based on error message patterns in responses.
- Provides a clear, formatted report of findings.
- Modular and extensible codebase.

## Usage

If you want to use GET request, type :
python scanner_tool.py "http://example.com/page?param1=value1&param2=value2"

If you want to use POST request, Type:
python scanner_tool.py "http://example.com/login" -X POST -d "username=admin&password=1234"

Install dependencies:

```bash
pip install requests
