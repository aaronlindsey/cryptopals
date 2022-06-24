#!/usr/bin/env python3

"""
Solution for cryptopals challenge 05 by Aaron Lindsey.
"""

import unittest

def repeating_key_xor(plaintext: bytes, key: bytes) -> bytes:
    return bytes([plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext))])

class TestChallenge05(unittest.TestCase):
    def test(self):
        plaintext = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
        key = b'ICE'
        ciphertext = bytes.fromhex('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
        self.assertEqual(repeating_key_xor(plaintext, key), ciphertext)

if __name__ == '__main__':
    unittest.main()
