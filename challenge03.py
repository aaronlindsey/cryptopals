#!/usr/bin/env python3

"""
Solution for https://cryptopals.com/sets/1/challenges/3 by Aaron Lindsey.
"""

import string
import unittest
from dataclasses import dataclass
from typing import Optional

from challenge02 import fixed_xor

# Source: The Adventures of Sherlock Holmes by Arthur Conan Doyle
# https://gutenberg.org/ebooks/1661
FREQUENCIES = {
    'a': 0.08155895644459231,
    'b': 0.014134945059007272,
    'c': 0.02482741412293105,
    'd': 0.04342833642925134,
    'e': 0.12617945234596653,
    'f': 0.021036069755191438,
    'g': 0.018575508054007598,
    'h': 0.06541166467973421,
    'i': 0.06320293511510346,
    'j': 0.0009819142938996552,
    'k': 0.008319702052547432,
    'l': 0.039921169610099165,
    'm': 0.026319923849658526,
    'n': 0.06776825898509338,
    'o': 0.07966443945400944,
    'p': 0.01601791011672073,
    'q': 0.000963431201308603,
    'r': 0.058746199414085966,
    's': 0.06256295803413828,
    't': 0.090809744286414,
    'u': 0.031190218747400814,
    'v': 0.0103389799181199,
    'w': 0.024915208812738548,
    'x': 0.0013099891873908343,
    'y': 0.02147042243108117,
    'z': 0.00034424759950834976
}


@dataclass
class CrackResult:
    score: float = float('inf')
    key: Optional[bytes] = None
    plaintext: Optional[bytes] = None
    ciphertext: Optional[bytes] = None


def crack_single_char_xor(ciphertext: bytes) -> CrackResult:
    result = CrackResult()

    for key in string.printable:
        padded_key = bytes([ord(key)] * len(ciphertext))
        plaintext = fixed_xor(ciphertext, padded_key)
        score = score_plaintext(plaintext)

        if score < result.score:
            result = CrackResult(score=score, key=bytes(
                [ord(key)]), plaintext=plaintext, ciphertext=ciphertext)

    return result


def score_plaintext(plaintext: bytes) -> int:
    score = 0

    for letter, expected_frequency in FREQUENCIES.items():
        actual_frequency = plaintext.count(ord(letter)) / len(plaintext)
        err = abs(actual_frequency - expected_frequency)
        score += err

    return score


class TestChallenge03(unittest.TestCase):
    def test_crack_single_char_xor(self):
        ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        result = crack_single_char_xor(ciphertext)
        self.assertEqual(result.plaintext, b"Cooking MC's like a pound of bacon")


if __name__ == '__main__':
    unittest.main()
