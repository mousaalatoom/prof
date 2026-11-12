# CSRF Mitigation Strategies

To properly protect web applications against Cross-Site Request Forgery (CSRF) attacks, developers should implement defense-in-depth protective measures:

## 1. Anti-CSRF Tokens (Synchronizer Token Pattern)
The most common and effective defense against CSRF is using Anti-CSRF tokens.
- Generate a unique, unpredictable, and secret token for each user session.
- Include this token as a hidden field in forms or in request headers.
- Validate the token on the server side for any state-changing request (POST, PUT, DELETE).

## 2. SameSite Cookie Attribute
Set the `SameSite` attribute on session cookies to prevent the browser from automatically sending cookies with cross-site requests:
- `SameSite=Strict`: Ensures the cookie is never sent in cross-site requests.
- `SameSite=Lax`: Withholds cookies on cross-site subrequests (e.g., images or frames), but sends them when a user navigates to the origin site.

## 3. Re-Authentication / Multi-Factor Verification
Require users to re-authenticate or confirm their actions (e.g., entering their current password or a One-Time Password / OTP) before executing sensitive actions such as transferring money or changing credentials.
