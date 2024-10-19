import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from loguru import logger


class AESEncryptor:
    """
    AES Encryptor class.
    """

    @staticmethod
    def encrypt_aes(plain_text: str, key: str) -> bytes:
        """
        Encryptor method.

        Args:
            * plain_text - Text to encrypt.
            * key - key for encryption. The value must contain 16, 24, or 32 characters.

        Returns:
            Encrypted text.
        """

        logger.info(f"Plain text: {plain_text}")
        if len(key) not in [16, 24, 32]:
            raise ValueError(f"The value must contain 16, 24, or 32 characters. Got: {len(key)}")
        init_vector = os.urandom(16)
        cipher = Cipher(algorithms.AES(key.encode("utf-8")), modes.CBC(init_vector), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        plaintext_bytes = plain_text.encode("utf-8")
        padded_data = padder.update(plaintext_bytes) + padder.finalize()
        cipher_text = encryptor.update(padded_data) + encryptor.finalize()
        crypted_text = init_vector + cipher_text
        logger.info(f"Crypted text: {crypted_text}")  # type: ignore[str-bytes-safe]
        return crypted_text

    @staticmethod
    def decrypt_aes(cipher_text: bytes, key: str) -> str:
        """
        Decryptor method.

        Args:
            * cipher_text - Encrypted text.
            * key - key for decryption. The value must contain 16, 24, or 32 characters.

        Returns:
            Decrypted text.
        """

        logger.info(f"Cipher text: {cipher_text}")  # type: ignore[str-bytes-safe]
        if len(key) not in [16, 24, 32]:
            raise ValueError(f"The value must contain 16, 24, or 32 characters. Got: {len(key)}")
        init_vector = cipher_text[:16]
        cipher_text = cipher_text[16:]
        cipher = Cipher(algorithms.AES(key.encode("utf-8")), modes.CBC(init_vector), backend=default_backend())
        decryptor = cipher.decryptor()
        plain_text = decryptor.update(cipher_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plain_text = unpadder.update(plain_text) + unpadder.finalize()
        logger.info(f"Plain text: {plain_text.decode('utf-8')}")
        return plain_text.decode("utf-8")
