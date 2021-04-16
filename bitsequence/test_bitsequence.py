from unittest import TestCase
from bitsequence import *


class LengthRelatedTestCase(TestCase):
    def test_returns0IfBitsequenceLengthIs0(self):
        possibilities = bitsequence(0)
        self.assertEqual(0, possibilities)

    def test_returns2IfBitsequenceLengthIs1(self):
        possibilities = bitsequence(1)
        self.assertEqual(2, possibilities)
