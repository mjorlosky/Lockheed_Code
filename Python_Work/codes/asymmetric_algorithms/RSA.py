from cryptography.hazmat.primitives.asymmetric import rsa
private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=2048,
)
print(private_key)

# Key Loading
from cryptography.hazmat.primitives import serialization

with open("path/to/key.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
	key_file.read(),
	password=None,
)

## Key Serialization
from cryptography.hazmat.primitives import serialization
pem = private_key.private_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PrivateFormat.PKCS8,
	encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)
pem.splitlines()[0]

# W/O Encryption
pem = private_key.private_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PrivateFormat.TraditionalOpenSSL,
	encryption_algorithm=serialization.NoEncryption()
)
pem.splitlines()[0]
# Public Keys
from cryptography.hazmat.primitives import serialization
public_key = private_key.public_key()
pem = public_key.public_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PublicFormat.SubjectPublicKeyInfo
)
pem.splitlines()[0]

## Signing
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
message = b"A message I want to sign"
signature = private_key.sign(
	message,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA256()),
		salt_length=padding.PSS.MAX_LENGTH
	),
	hashes.SHA256()
)

# Large data to hash
from cryptography.hazmat.primitives.asymmetric import utils
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash)
hasher.update(b"data & ")
hasher.update(b"more data")
digest = hasher.finalize()
sig = private_key.sign(
	digest,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA256()),
		salt_length=padding.PSS.MAX_LENGTH
	),
	utils.Prehashed(chosen_hash)
)

## Verification
public_key = private_key.public_key()
public_key.verify(
	signature,
	message,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA256()),
		salt_length=padding.PSS.MAX_LENGTH
	),
	hashes.SHA256()
)

# Large data
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash)
hasher.update(b"data & ")
hasher.update(b"more data")
digest = hasher.finalize()
public_key.verify(
	sig,
	digest,
	padding.PSS(
	mgf=padding.MGF1(hashes.SHA256()),
	salt_length=padding.PSS.MAX_LENGTH
	),
	utils.Prehashed(chosen_hash)
)

## Encryption 
message = b"encrypted data"
ciphertext = public_key.encrypt(
	message,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)





