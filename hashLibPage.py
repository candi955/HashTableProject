# reference: https://docs.python.org/3/library/hashlib.html
# https://pypi.org/project/hashlib/
# https://readthedocs.org/projects/hashlib/
# https://circuitpython.readthedocs.io/projects/hashlib/en/latest/
# https://github.com/adafruit/Adafruit_CircuitPython_hashlib
# https://www.pythoncentral.io/hashing-strings-with-python/

# Other references for hash tables in python:
# https://www.geeksforgeeks.org/python-hash-method/'
# https://www.geeksforgeeks.org/applications-of-hashing/

import hashlib

m = hashlib.sha256()
print(m.update(b"Nobody inspects"))
print(m.update(b" the spammish repetition"))
print(m.digest())
# b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
print(m.digest_size)

print(m.block_size)

print(hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest())

# reference: https://www.pythoncentral.io/hashing-strings-with-python/
print("\n\nHash object:")
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())