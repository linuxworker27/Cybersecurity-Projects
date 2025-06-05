# report.py

def generate_report(vulnerabilities):
    if not vulnerabilities:
        print("No SQL Injection vulnerabilities found.")
        return

    print("\n--- SQL Injection Vulnerability Report ---\n")
    for i, vuln in enumerate(vulnerabilities, 1):
        print(f"Vulnerability {i}:")
        print(f"URL: {vuln['url']}")
        print(f"Parameter: {vuln['parameter']}")
        print(f"Payload: {vuln['payload']}")
        print(f"Reason: {vuln['reason']}")
        print("-" * 40)
