import base64

token_val = "th0n24f1qi77p4v43mapi87nr0"

token_val += "=" * ((4 - len(token_val) % 4) % 4)
old_iv = base64.b64decode(token_val)
new_iv = bytearray(old_iv)

for i, (o, t) in enumerate(zip(b"guest", b"admin")):
    new_iv[i] = old_iv[i] ^ o ^ t

print("New Token:", base64.b64encode(new_iv).decode())
