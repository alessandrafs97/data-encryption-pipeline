from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64


def encrypt_value(value: str, key: bytes, iv: bytes) -> str:
    """
    Encrypt a single value using AES-256.

    :param value: Plain text value to encrypt
    :param key: 32-byte encryption key
    :param iv: 16-byte initialization vector
    :return: Base64 encoded encrypted value
    """

    if value is None:
        return None

    # PKCS7 
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(value.encode("utf-8")) + padder.finalize()

    # AES encryption
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv)
