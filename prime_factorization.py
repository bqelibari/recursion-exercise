from math import sqrt, floor


def factorize(num: int) -> list[int]:
    prime_factors = return_list_of_primefactors_and_rest(num)
    prime_factors = remove_last_item_if_num_fully_dividable_by_prime(prime_factors)
    return prime_factors


def remove_last_item_if_num_fully_dividable_by_prime(prime_factors: list[str]) -> list[str]:
    if prime_factors[-1] == '1':
        return prime_factors[0:-1]
    return prime_factors


def return_list_of_primefactors_and_rest(num: int):
    result = []
    for divisor in range(2, int(sqrt(num)) + 1):
        while num % divisor == 0:
            result.append(str(divisor))
            num = num / divisor
    rest_as_string = str(int(num))
    result.append(rest_as_string)
    return result
