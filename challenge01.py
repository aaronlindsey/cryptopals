#!/usr/bin/env python3

import base64
import unittest

def hex_to_base64(s):
    return base64.b64encode(bytes.fromhex(s)).decode("utf-8")

class Test(unittest.TestCase):

    def test_hex_to_base64(self):
        expect = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        actual = hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
