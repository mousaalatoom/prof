# Exercise 00: XSS Vulnerability Analysis

## 📌 Project Overview
This project focuses on identifying and demonstrating a **Cross-Site Scripting (XSS)** vulnerability within a web application environment[span_0](start_span)[span_0](end_span). The objective is to analyze how untrusted user input is processed, successfully exploit the vulnerability to reveal session cookies, and document remediation strategies[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span).

---

## 🔍 Vulnerability Details
* **Vulnerability Type:** Cross-Site Scripting (XSS)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
* **Category:** OWASP Top 10 - Injection / Web Application Security[span_5](start_span)[span_5](end_span)
* **Impact:** High (Potential for session hijacking, user impersonation, and unauthorized data access)[span_6](start_span)[span_6](end_span)

### Description
The target application fails to sanitize or encode user input submitted through the input field before rendering it in the DOM[span_7](start_span)[span_7](end_span). As a result, an attacker can inject malicious client-side JavaScript code that executes within the context of the user's browser session[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).

---

## 🛡️ OWASP Context
In the **OWASP Top 10**, XSS is highlighted as a critical threat. When applications lack proper input validation and output encoding, attackers can manipulate the application's response to perform actions on behalf of users or exfiltrate sensitive data such as session cookies[span_10](start_span)[span_10](end_span).
