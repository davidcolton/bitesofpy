import base64
from cryptography.fernet import Fernet  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from os import urandom
from typing import ByteString, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ClamyFernet:
    password: ByteString = b"pybites"
    key: Optional[ByteString] = None

    def __post_init__(self):
        """Initializes the class"""
        self.salt = urandom(16)
        self.algorithm = hashes.SHA512()
        self.length = 32
        self.iterations = 100_000
        self.backend = default_backend()

        if self.key is None:
            self.key = base64.urlsafe_b64encode(self.kdf.derive(self.password))

    @property
    def kdf(self):
        return PBKDF2HMAC(
            algorithm=self.algorithm,
            length=self.length,
            salt=self.salt,
            iterations=self.iterations,
            backend=self.backend,
        )

    @property
    def clf(self):
        return Fernet(self.key)

    def encrypt(self, message: str) -> ByteString:
        return self.clf.encrypt(str.encode(message))

    def decrypt(self, token: ByteString) -> str:
        return self.clf.decrypt(token).decode("utf-8")
