#!/usr/bin/env python3

import unittest

def fixed_XOR(a, b):
    return format(int(a, 16) ^ int(b, 16), 'x') # format instead of hex() to strip the 0x

class Test(unittest.TestCase):

    def test_fixed_XOR(self):
        expect = '746865206b696420646f6e277420706c6179'
        actual = fixed_XOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
