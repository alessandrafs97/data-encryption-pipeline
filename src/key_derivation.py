from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os


def derive_key(password: bytes, salt: bytes, iterations: int = 100_000) -> bytes:
    """
    Derive a 256-bit key using PBKDF2 (HMAC + SHA256).

    :param password: Base secret (password / passphrase)
    :param salt: Random salt
    :param iterations: Number of derivation iterations
    :return: 32-byte derived key
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,   # 256 bits
        salt=salt,
        iterations=iterations,
    )

    return kdf.derive(password)


def generate_salt(length: int = 16) -> bytes:
    """
    Generate a random salt.

    :param length: Salt size in bytes
    """
    return os.urandom(length)
