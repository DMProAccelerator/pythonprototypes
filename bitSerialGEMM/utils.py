import pprint
import itertools
from operator import add

def _print(obj, desc=None):
    if desc:
        print(desc, end=": ")
    pprint.PrettyPrinter().pprint(obj)

def to_bitstring(M):
    if isinstance(M, int):
        # int
        return bin(M)[2:]

    d = __bit_depth(M)
    if any(isinstance(e, list) for e in M): 
        # matrix
        return [[__pad_zeroes(bin(e)[2:], d) for e in row] for row in M]
    else:
        # vector
        return [__pad_zeroes(bin(e)[2:], d) for e in M]

def _xor(a, b):
    pass

def _and(a, b):
    """Logical AND for bitstrings """
    res = []
    for x, y in itertools.zip_longest(a, b, fillvalue="0"):
        if x == "1" and y == "1":
            res.append("1")
        else:
            res.append("0")
    return "".join(res)


def transpose(M):
    return list(map(list, zip(*M)))

def __pad_zeroes(b, n):
    return b.zfill(n)

def __bit_depth(M):
    if any(isinstance(e, list) for e in M): 
        # matrix
        return max(len(bin(e)[2:]) for row in M for e in row)
    else:
        # vector
        return max(len(bin(e)[2:]) for e in M)

def flatten(L):
    return list(itertools.chain.from_iterable(L))

def popcount(b):
    return b.count("1")

def add_lists(a, b):
    return list(map(add, a, b))

def test_to_bitstring():
    a = [[1, 3], [0, 2]]
    assert to_bitstring(a) == [["01", "11"], ["00", "10"]]

    b = [[2], [2]]
    assert to_bitstring(b) == [["10"], ["10"]]

    c = [1,0,0,1,0]
    assert to_bitstring(c) == ["1", "0", "0", "1", "0"]

def test_and():
    assert _and("0", "0") == "0"
    assert _and("0", "1") == "0"
    assert _and("1", "0") == "0"
    assert _and("1", "1") == "1"

    for i, j in zip(range(1000, 0, -1), range(0, 1000)):
        print(i, j)    


if __name__ == "__main__":
    test_to_bitstring()
    test_and()

