#!/usr/bin/env python3
#
# /// script
# dependencies = [
#   "cryptography",
#   "PyJWT",
# ]
# ///

import sys
import jwt
import datetime

if len(sys.argv) != 3:
    print("Usage: python genjwt.py <private_key.pem> <public_key.pem>")
    sys.exit(1)

priv_path, pub_path = sys.argv[1], sys.argv[2]

with open(priv_path, "r") as f:
    private_key = f.read()

with open(pub_path, "r") as f:
    public_key = f.read()

payload = {
    "sub": "1234567890",
    "name": "htsget",
    "admin": True,
    "iat": datetime.datetime.utcnow()
}

token = jwt.encode(payload, private_key, algorithm="RS256")
print("JWT:", token)

decoded = jwt.decode(token, public_key, algorithms=["RS256"])
print("Decoded:", decoded)