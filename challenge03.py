#!/usr/bin/env python3

"""
Solution for https://cryptopals.com/sets/1/challenges/3 by Aaron Lindsey.
"""

import string
import unittest
from challenge02 import fixed_xor

PRINTABLE_BYTES = set(bytes(string.printable, 'ascii'))

def crack_single_char_xor(ciphertext: bytes) -> bytes:
    max_score = -1
    keys = [bytes([ord(c)] * len(ciphertext)) for c in string.printable]

    for key in keys:
        plaintext = fixed_xor(ciphertext, key)
        plaintext_score = score_plaintext(plaintext)
        if max_score < plaintext_score:
            max_score = plaintext_score
            result = plaintext

    return result

def score_plaintext(plaintext: bytes) -> bytes:
    score = 0

    for b in plaintext:
        if b not in PRINTABLE_BYTES:
            return 0

        c = chr(b)
        if c.islower():
            score += 4
        elif c.isupper():
            score += 2
        elif c.isnumeric() or c.isspace():
            score += 1

    return score

class TestChallenge03(unittest.TestCase):
    def test_crack_single_char_xor(self):
        ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        self.assertEqual(crack_single_char_xor(ciphertext), b"Cooking MC's like a pound of bacon")

if __name__ == '__main__':
    unittest.main()
