#!/usr/bin/env python3

import base64
import unittest

def hex_to_base64(data: bytes) -> bytes:
    return base64.b64encode(base64.b16decode(data, casefold=True))

class TestChallenge01(unittest.TestCase):
    def test_hex_to_base64(self):
        original = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        encoded = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_base64(original), encoded)

if __name__ == '__main__':
    unittest.main()
