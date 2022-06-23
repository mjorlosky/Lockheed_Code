from cryptography.hazmat.primitives import constant_time
import timeit
print(timeit.timeit(lambda: constant_time.bytes_eq(b"foo", b"foo")))
print(timeit.timeit(lambda: constant_time.bytes_eq(b"foo", b"bar")))