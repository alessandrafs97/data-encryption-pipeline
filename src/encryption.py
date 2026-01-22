import base64
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


IV = bytes([0] * 16)  # IV fixo, igual ao JETL


def derive_key(secret_key: str, salt: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,           # AES-256
        salt=salt.encode(),
        iterations=65536
    )
    return kdf.derive(secret_key.encode())


def encrypt_value(value: str, key: bytes) -> str:
    if not value:
        return ""

    padder = padding.PKCS7(128).padder()
    padded_value = padder.update(value.encode()) + padder.finalize()

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(IV)
    )

    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_value) + encryptor.finalize()

    return base64.b64encode(encrypted).decode()
