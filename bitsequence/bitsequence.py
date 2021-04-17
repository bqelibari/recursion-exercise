from functools import cache

@cache
def get_bitsequence_possibilities(sequence_length: int):
    if sequence_length <= 0: return 0
    if sequence_length == 1: return 2
    if sequence_length == 2: return 3
    previous_result = get_bitsequence_possibilities(sequence_length - 1)
    previous_zeros = get_bitsequence_possibilities(sequence_length - 2)
    return previous_result + previous_zeros
