import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
data = b"a secret message"
aad = b"authenticated but unencrypted data"
key = ChaCha20Poly1305.generate_key()
chacha = ChaCha20Poly1305(key)
nonce = os.urandom(12)
print()
ct = chacha.encrypt(nonce, data, aad)
print(ct)
print()
print(chacha.decrypt(nonce, ct, aad))

sentence = b"Bush did 9/11"
auth = b"randomdata"
key2 = ChaCha20Poly1305.generate_key()
chachaslide = ChaCha20Poly1305(key2)
nonce2 = os.urandom(12)
print()
ct2 = chachaslide.encrypt(nonce2, sentence, auth)
print(ct2)
print()
print(chachaslide.decrypt(nonce2, ct2, auth))


from cryptography.hazmat.primitives.ciphers.aead import AESGCM
data = b"a secret message"
aad = b"authenticated but unencrypted data"
key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
print()
ct = aesgcm.encrypt(nonce, data, aad)
print(ct)
print()
print(aesgcm.decrypt(nonce, ct, aad))