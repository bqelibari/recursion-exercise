from math import sqrt, floor


def factorize(num: int) -> list[int]:
    result, num = return_list_of_twos_and_new_num(num)
    other_factors, rest = return_list_of_other_primefactors_and_rest(num)
    result.extend(other_factors)
    result.append(int(rest))
    if result[-1] == 1:
        return result[0:-1]
    return result


def return_list_of_twos_and_new_num(num):
    result = []
    while num % 2 == 0:
        result.append(2)
        num = num / 2
    return result, num


def return_list_of_other_primefactors_and_rest(num: int):
    result = []
    for divisor in range(3, int(sqrt(num)) + 1):
        while num % divisor == 0:
            result.append(divisor)
            num = num / divisor
    return result, num