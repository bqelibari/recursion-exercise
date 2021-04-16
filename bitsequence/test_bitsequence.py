from unittest import TestCase
from bitsequence import *


class LengthRelatedTestCase(TestCase):
    def test_returns0IfBitsequenceLengthIs0(self):
        possibilities = bitsequence(0)
        self.assertEqual(0, possibilities)
