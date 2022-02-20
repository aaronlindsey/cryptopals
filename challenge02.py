#!/usr/bin/env python3

import sys
import unittest

# 200000 loops, best of 5: 1.74 usec per loop
def fixed_XOR(a: bytes, b: bytes) -> bytes:
    a_int = int.from_bytes(a, sys.byteorder)
    b_int = int.from_bytes(b, sys.byteorder)
    result = a_int ^ b_int
    return int.to_bytes(result, len(a), sys.byteorder)

# 100000 loops, best of 5: 3.94 usec per loop
def fixed_XOR_zip(a: bytes, b: bytes) -> bytes:
    return bytes(byte_1 ^ byte_2 for byte_1, byte_2 in zip(a, b))

class TestChallenge02(unittest.TestCase):
    msg = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    key = bytes.fromhex('686974207468652062756c6c277320657965')
    out = bytes.fromhex('746865206b696420646f6e277420706c6179')

    def test_fixed_XOR(self):
        self.assertEqual(fixed_XOR(self.msg, self.key), self.out)

    def test_fixed_XOR_zip(self):
        self.assertEqual(fixed_XOR_zip(self.msg, self.key), self.out)

if __name__ == '__main__':
    unittest.main()
