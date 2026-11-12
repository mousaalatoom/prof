
`Fix.md`

```bash
cat > Fix.md <<'EOF'
# Fix - Exercise 02

## 1. Problem

The application uses AES-128-CBC encryption but does not authenticate
the encrypted data and its Initialization Vector (IV).

The IV is received from a client-controlled cookie.

CBC encryption does not provide integrity protection. Therefore, an
attacker can modify the IV and change the first decrypted plaintext
block without knowing the encryption key.

The application also derives the admin privilege from decrypted
identity data.

## 2. Recommended Solution

### A. Use Authenticated Encryption

Replace AES-CBC with an authenticated encryption mode such as
AES-256-GCM.

Authenticated encryption verifies the integrity of encrypted data
before accepting the decrypted plaintext.

If CBC must be retained, use Encrypt-then-MAC with a secure MAC such
as HMAC-SHA-256. Verify the MAC before decrypting.

### B. Do Not Trust Client-Controlled Identity Data

Do not determine user privileges from a value that the client can
modify.

Store the authenticated user identity and authorization state
in a secure server-side session.

The server must perform authorization checks using trusted
server-side data.

### C. Protect Session Cookies

Session cookies should use appropriate security attributes:

- HttpOnly
- Secure (when using HTTPS)
- SameSite

Use secure session handling and regenerate the session identifier
after authentication.

### D. Use Secure Random IVs

Generate IVs using a cryptographically secure random number generator.

An IV should not be treated as secret, but its integrity must be
protected when using an encryption mode that requires authentication.

## 3. Example Secure Design

A safer design is:

1. Authenticate the user.
2. Store the user's identity and role in a server-side session.
3. Generate a new secure session identifier after login.
4. Read authorization information from trusted server-side storage.
5. Never grant admin privileges based only on a client-controlled cookie.

## 4. Additional Improvements

- Use prepared statements for database queries.
- Avoid exposing internal cryptographic errors to users.
- Keep encryption keys outside source code.
- Use modern, supported PHP versions and cryptographic libraries.
- Log authentication and authorization failures safely.

## 5. Conclusion

The vulnerability can be prevented by using authenticated encryption
and by keeping authorization decisions on the server.

Encryption without integrity protection is not sufficient to protect
sensitive identity data.
EOF
