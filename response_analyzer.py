# response_analyzer.py

import re

# Common SQL error patterns to detect in responses
sql_errors = [
    r"you have an error in your sql syntax;",
    r"warning: mysql",
    r"unclosed quotation mark after the character string",
    r"quoted string not properly terminated",
    r"pg_query\(\): query failed:",
    r"mysql_fetch_array\(\)",
    r"syntax error",
    r"sqlstate",
    r"mysql_num_rows\(\)",
    r"mysql_query\(\)",
    r"mysql_result\(\)",
    r"ORA-01756",
    r"SQL syntax.*?MySQL",
    r"Microsoft OLE DB Provider for SQL Server",
    r"Incorrect syntax near",
]

def analyze_response(response):
    if response is None:
        return False, "No response"

    content = response.text.lower()
    for pattern in sql_errors:
        if re.search(pattern, content):
            return True, f"SQL error pattern found: {pattern}"
    return False, "No SQL error patterns detected"
