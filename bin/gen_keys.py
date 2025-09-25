#!/usr/bin/env python3
#
# /// script
# dependencies = [
#   "cryptography",
#   "PyJWT[crypto]",
# ]
# ///

import datetime
from pathlib import Path

import jwt as pyjwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# --- Config ---
KEY_DIR = Path("data/keys")
PRIVATE_KEY_FILE = KEY_DIR / "private.pem"
PUBLIC_KEY_FILE = KEY_DIR / "public.pem"
JWT_FILE = KEY_DIR / "jwt_bearer_token.txt"


def save_file(path: Path, content: bytes) -> None:
    """Write bytes to a file, creating parent dirs if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def generate_keys() -> tuple[str, str]:
    """Generate RSA private/public key pair (PKCS8, 4096 bits)."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )

    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    save_file(PRIVATE_KEY_FILE, priv_pem)
    save_file(PUBLIC_KEY_FILE, pub_pem)

    return priv_pem.decode(), pub_pem.decode()


def generate_jwt(private_key: str) -> str:
    """Generate a RS256 JWT using the provided private key."""
    payload = {
        "sub": "1234567890",
        "name": "htsget",
        "admin": True,
        "iat": datetime.datetime.utcnow(),
    }
    return pyjwt.encode(payload, private_key, algorithm="RS256")


def validate_jwt(token: str, public_key: str) -> dict:
    """Validate JWT using the public key."""
    return pyjwt.decode(token, public_key, algorithms=["RS256"])


def main() -> None:
    priv_key, pub_key = generate_keys()
    token = generate_jwt(priv_key)

    save_file(JWT_FILE, token.encode())

    decoded = validate_jwt(token, pub_key)

    print(f"Keys saved in: {KEY_DIR.resolve()}")
    print(f"JWT saved in: {JWT_FILE.resolve()}")
    print("Decoded payload:", decoded)


if __name__ == "__main__":
    main()
