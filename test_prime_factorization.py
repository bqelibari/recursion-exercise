from unittest import TestCase
from prime_factorization import *


class PrimeFactorizationTestCase(TestCase):
    def test_returnsPrimeIfNumIsPrime(self):
        self.assertEqual('2', factorize(2))
