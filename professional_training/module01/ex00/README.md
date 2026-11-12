## Overview
This project demonstrates a **Server-Side Template Injection (SSTI)** vulnerability. SSTI occurs when user-supplied input is insecurely concatenated or embedded directly into a web template engine, allowing an attacker to execute arbitrary code or access sensitive system files on the server.

## Vulnerability Description
Based on OWASP guidelines, injection flaws like SSTI arise when web applications fail to properly sanitize or contextually escape user input before passing it to a template renderer (such as Jinja2, Twig, or FreeMarker). 

## Real-World Exploitation Scenarios
1. **Remote Code Execution (RCE):** Attackers can escalate template injection to execute system shell commands, taking full control of the underlying server infrastructure.
2. **Sensitive Information Disclosure:** Unauthorized reading of system configuration files, environment variables, or critical credentials (such as `/etc/passwd`).
