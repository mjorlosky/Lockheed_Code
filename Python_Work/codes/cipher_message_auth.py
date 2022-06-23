#!/usr/bin/env python3
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
key = b"passwordpassword"
c = cmac.CMAC(algorithms.AES(key))
c.verify(b"passwordpassword")