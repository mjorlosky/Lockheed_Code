import os
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1
key = os.urandom(20)
hotp = HOTP(key, 6, SHA1())
hotp_value = hotp.generate(0)
hotp.verify(hotp_value, 0)
print(key)
print(hotp)
print(hotp_value)
print()

import time
from cryptography.hazmat.primitives.twofactor.totp import TOTP
key = os.urandom(20)
totp = TOTP(key, 8, SHA1(), 30)
time_value = time.time()
totp_value = totp.generate(time_value)
totp.verify(totp_value, time_value)
print(key)
print(totp)
print(time_value)
print(totp_value)