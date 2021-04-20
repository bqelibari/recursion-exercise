from unittest import TestCase
from prime_factorization import *


class PrimeFactorizationTestCase(TestCase):
    def test_returnsPrimeIfNumIsPrime(self):
        self.assertEqual([2], factorize(2))
        self.assertEqual([3], factorize(3))
        self.assertEqual([5], factorize(5))

    def test_returnListOfTwosAndNewNum(self):
        self.assertEqual(([2, 2], 1), return_list_of_twos_and_new_num(4))
        self.assertEqual(([2, 2], 141), return_list_of_twos_and_new_num(564))

    def test_sixReturnsItsPrimefactorization(self):
        self.assertEqual([2, 3], factorize(6))

    def test_nineReturnsPrimefactorization(self):
        self.assertEqual([3, 3], factorize(9))

    def test_returnListOfOtherPrimefactorsAndRest(self):
        self.assertEqual(([], 3), return_list_of_other_primefactors_and_rest(3))
        self.assertEqual(([], 5), return_list_of_other_primefactors_and_rest(5))
        self.assertEqual(([3], 47), return_list_of_other_primefactors_and_rest(141))
        self.assertEqual(([7], 257), return_list_of_other_primefactors_and_rest(1799))