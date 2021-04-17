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
