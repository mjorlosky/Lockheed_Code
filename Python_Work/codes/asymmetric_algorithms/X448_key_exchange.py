from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x448 import X448PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
# Generate a private key for use in the exchange.
private_key = X448PrivateKey.generate()
# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key and
# get a public key from that. Note that in a DH handshake both peers
# must agree on a common set of parameters.
peer_public_key = X448PrivateKey.generate().public_key()
shared_key = private_key.exchange(peer_public_key)
# Perform key derivation.
derived_key = HKDF(
	algorithm=hashes.SHA256(),
	length=32,
	salt=None,
	info=b'handshake data',
).derive(shared_key)

# For the next handshake we MUST generate another private key.
private_key_2 = X448PrivateKey.generate()
peer_public_key_2 = X448PrivateKey.generate().public_key()
shared_key_2 = private_key_2.exchange(peer_public_key_2)
derived_key_2 = HKDF(
	algorithm=hashes.SHA256(),
	length=32,
	salt=None,
	info=b'handshake data',
).derive(shared_key_2)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x448
private_key = x448.X448PrivateKey.generate()
private_bytes = private_key.private_bytes(
	encoding=serialization.Encoding.Raw,
	format=serialization.PrivateFormat.Raw,
	encryption_algorithm=serialization.NoEncryption()
)
loaded_private_key = x448.X448PrivateKey.from_private_bytes(private_bytes)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x448
private_key = x448.X448PrivateKey.generate()
public_key = private_key.public_key()
public_bytes = public_key.public_bytes(
	encoding=serialization.Encoding.Raw,
	format=serialization.PublicFormat.Raw
)
loaded_public_key = x448.X448PublicKey.from_public_bytes(public_bytes)

