from hashlib import md5, sha256
from binascii import unhexlify


class BloomFilter:
    def __init__(self):
        self.vector = 0

    def get_hash(self, value):
        return int.from_bytes(
            unhexlify(md5(value.encode("UTF-8")).hexdigest()),
            byteorder='little')

    def add(self, value):
        hashed = self.get_hash(value)
        self.vector |= hashed

    def check(self, value):
        hashed = self.get_hash(value)
        for a, b in zip(bin(hashed)[2:], bin(self.vector)[2:]):
            if bool(int(a)) and not bool(int(b)):
                return False
        return True


# Tests
bf = BloomFilter()
bf.add("test1")
bf.add("test2")
assert bf.check("test1")
assert not bf.check("test3")
