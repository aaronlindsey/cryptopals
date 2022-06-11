#!/usr/bin/env python3

import base64
import unittest
from challenge02 import fixed_XOR

def decrypt(ciphertext: bytes) -> bytes:
    keys = range(ord('A'), ord('Z'))
    max_score = -1
    for key in keys:
        padded_key = bytes([key] * len(ciphertext))
        plaintext = fixed_XOR(ciphertext, padded_key)
        plaintext_score = score(plaintext)
        if max_score < plaintext_score:
            max_score = plaintext_score
            result = plaintext
    return result

def score(plaintext: bytes) -> bytes:
    return sum(chr(c).isalpha() for c in plaintext)

class TestChallenge03(unittest.TestCase):
    def test(self):
        ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        plaintext = decrypt(ciphertext)
        self.assertEqual(plaintext, b"Cooking MC's like a pound of bacon")
        pass

if __name__ == '__main__':
    unittest.main()
