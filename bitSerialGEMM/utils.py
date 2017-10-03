import pprint, itertools, bitstring
from operator import add

def int_to_bits(i, length=64):
    return bitstring.Bits(int=i, length=length)

def to_bitstring(M):
    if isinstance(M, int):
        return int_to_bits(M)

    # +1 for signed integers
    d = __bit_depth(M) + 1
    if is_matrix(M):
        return [[int_to_bits(i, length=d) for i in row] for row in M]
    else:
        return [int_to_bits(i, length=d) for i in M]

def transpose(M):
    return list(map(list, zip(*M)))

def __bit_depth(M):
    if is_matrix(M): 
        return max(len(bin(e)[2:]) for e in flatten(M))
    else:
        return max(len(bin(e)[2:]) for e in M)

def is_matrix(M):
    return any(isinstance(e, list) for e in M)

def flatten(L):
    return list(itertools.chain.from_iterable(L))

def add_lists(a, b):
    return list(map(add, a, b))

