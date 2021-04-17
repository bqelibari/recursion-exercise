from unittest import TestCase
from bitsequence import *


class LengthRelatedTestCase(TestCase):
    def test_returns0IfBitsequenceLengthIs0(self):
        possibilities = get_bitsequence_possibilities(0)
        self.assertEqual(0, possibilities)

    def test_returns2IfBitsequenceLengthIs1(self):
        possibilities = get_bitsequence_possibilities(1)
        self.assertEqual(2, possibilities)

    def test_returns3fIfBitsequenceLengthIs2(self):
        possibilities = get_bitsequence_possibilities(2)
        self.assertEqual(3, possibilities)

    def test_returns5IfBitsequenceLengthIs3(self):
        possibilities = get_bitsequence_possibilities(3)
        self.assertEqual(5, possibilities)

    def test_returns8IfBitsequenceLengthIs4(self):
        possibilities = get_bitsequence_possibilities(4)
        self.assertEqual(8, possibilities)

    def test_returns13IfBitsequenceLengthIs5(self):
        possibilities = get_bitsequence_possibilities(5)
        self.assertEqual(13, possibilities)

    def test_returns13IfBitsequenceLengthIs6(self):
        possibilities = get_bitsequence_possibilities(6)
        self.assertEqual(21, possibilities)