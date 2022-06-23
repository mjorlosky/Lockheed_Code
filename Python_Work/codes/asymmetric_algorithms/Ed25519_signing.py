from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(b"my authenticated message")
public_key = private_key.public_key()
# Raises InvalidSignature if verification fails
public_key.verify(signature, b"my authenticated message")

# Key Interfaces
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
private_key = ed25519.Ed25519PrivateKey.generate()
private_bytes = private_key.private_bytes(
	encoding=serialization.Encoding.Raw,
	format=serialization.PrivateFormat.Raw,
	encryption_algorithm=serialization.NoEncryption()
)
loaded_private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes)

public_key = private_key.public_key()
public_bytes = public_key.public_bytes(
	encoding=serialization.Encoding.Raw,
	format=serialization.PublicFormat.Raw
)
loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes)
# public_key.verify(signature, loaded_public_key)
# private_key.verify(signature, loaded_private_key)