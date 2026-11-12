# Fix Report: SSRF & LFI Mitigation

## 1. Vulnerability Overview
- **LFI:** Allowed local file reading via the `file:///` scheme and Python's `open()` function.
- **SSRF:** Allowed uncontrolled outgoing requests to internal/external endpoints.

## 2. Remediation Steps
- **Remove File Handlers:** Completely delete local file reading logic and `file://` scheme processing.
- **Enforce Allowlist:** Restrict URL schemes strictly to `http` and `https`.
- **Block Internal IPs:** Prevent requests to loopback addresses (`127.0.0.1`, `localhost`) and metadata services.

## 3. Secure Code Example
```python
from urllib.parse import urlparse
import requests

@app.route('/fetch', methods=['GET'])
def fetch():
    url = request.args.get('url')
    parsed = urlparse(url)
    
    # Enforce protocols and block internal hosts
    if parsed.scheme not in ['http', 'https']:
        return "Error: Protocol not allowed", 403
    if parsed.hostname in ['localhost', '127.0.0.1', '169.254.169.254']:
        return "Error: Internal access forbidden", 403
        
    response = requests.get(url, allow_redirects=False, timeout=5)
    return response.text
