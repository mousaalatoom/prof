Cross-Site Request Forgery (CSRF) Vulnerability
Overview
Cross-Site Request Forgery (CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same-origin policy, which is designed to prevent different websites from interfering with each other.

In a successful CSRF attack, the attacker causes the victim user to carry out an action state-changing request (such as transferring funds, changing email addresses, or updating credentials) while authenticated.

OWASP Alignment
According to the OWASP Top 10, CSRF occurs when a web application processes a request from a browser without verifying whether the request was intentionally sent by the user. Because browsers automatically include session identifiers and credentials with cross-origin requests, applications that rely solely on these mechanisms are vulnerable to exploitation.

