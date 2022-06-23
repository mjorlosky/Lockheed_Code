from cryptography.hazmat.primitives import poly1305
key = b"pollpollpollpollpollpollpollpoll"
p = poly1305.Poly1305(key)
p.update(b"message to authenticate")
print(p.verify(key))
p.finalize()