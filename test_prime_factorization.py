from unittest import TestCase
from prime_factorization import *


class PrimeFactorizationTestCase(TestCase):
    def test_returnsNoneIfNumLowerThan2(self):
        factors = factorize(1)
        self.assertEqual(None, factors)
