# Exercise 02 - CBC IV Bit-Flipping

## 1. Overview

This exercise demonstrates a weakness in the way the application handles
AES-128-CBC encrypted identity data.

The application uses an encrypted identity value and a client-controlled
cookie named `token`, which is used as the Initialization Vector (IV)
during decryption.

The application does not authenticate the IV and ciphertext together.
As a result, an attacker can modify the IV and change the decrypted
plaintext without knowing the encryption key.

## 2. Vulnerability

The application uses AES-128-CBC encryption.

In CBC mode, the first plaintext block is calculated as:

P1 = D(K, C1) XOR IV

Where:
- P1 is the first plaintext block.
- D is the block cipher decryption operation.
- K is the encryption key.
- C1 is the first ciphertext block.
- IV is the Initialization Vector.

Changing the IV changes the first plaintext block after decryption.

The application stores the encrypted identity in the server-side PHP
session but accepts the IV from the client's `token` cookie.

The application does not verify the integrity of this value.

## 3. Exploitation

We first logged in using the test account:

- Username: guest
- Password: guestpass

After successful login, the application created a `token` cookie.

We modified the IV so that the decrypted identity changed from `guest`
to `admin`.

The modification was calculated using:

IV_new = IV_old XOR "guest" XOR "admin"

After replacing the `token` cookie with the modified value and
reloading the page, the application treated the session as admin.

The flag was displayed successfully.

## 4. Result

The attack succeeded and demonstrated that changing the client-controlled
IV can modify the decrypted identity.

This is a CBC IV Bit-Flipping vulnerability caused by missing
cryptographic integrity protection.

## 5. Conclusion

Encryption alone does not guarantee data integrity.

Applications must authenticate encrypted data and must not trust
client-controlled values when determining user privileges.

This exercise was completed without using SQL injection.
EOF
