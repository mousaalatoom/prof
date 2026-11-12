# Vulnerability Report: SSRF and LFI

## Overview
This project contains a deliberate security vulnerability combining **SSRF (Server-Side Request Forgery)** and **LFI (Local File Inclusion)**.

## Vulnerability Type
- **SSRF (Server-Side Request Forgery):** Occurs when a web application fetches a remote resource from a user-supplied URL without validating the destination.
- **LFI (Local File Inclusion):** Occurs when user input allows direct access to local system files via insecure file reading handlers (e.g., using `file:///` scheme and Python's `open()` function).

## Explanation
The backend code (`app.py`) accepts a `url` parameter. By using the `file:///` prefix, the application intercepts the input, strips the prefix, and directly reads local files from the server's disk (such as `/etc/passwd`), exposing sensitive system files.
