import os
from cryptography.hazmat.primitives import hashes, hmac
key = os.urandom(32)
h = hmac.HMAC(key, hashes.SHA256())
h.update(b"message to hash")
h.verify(b"message to hash")
