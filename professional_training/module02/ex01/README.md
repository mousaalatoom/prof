Overview
This exercise demonstrates a common security vulnerability known as Insecure Deserialization. The vulnerable Flask application accepts serialized data from user input and deserializes it without proper validation or sanitization.

Vulnerability Description
In Python, libraries like pickle are used to serialize and deserialize object structures. However, pickle is inherently insecure by design. When untrusted user input is passed into pickle.loads(), an attacker can craft malicious serialized payloads containing arbitrary Python code (e.g., using the __reduce__ magic method) that will be executed on the server with the privileges of the application process.

Objective
The main objective of this challenge is to exploit this deserialization flaw to read the contents of the sensitive system file /etc/passwd.
