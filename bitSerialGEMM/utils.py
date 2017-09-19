import pprint

def _print(obj, desc=None):
    if desc:
        print(desc, end=": ")
    pprint.PrettyPrinter().pprint(obj)

def _to_bitstring(M):
    d = __bit_depth(M)
    return [[__pad_zeroes(bin(e)[2:], d) for e in row] for row in M]

def __pad_zeroes(b, n):
    return b.zfill(n)

def __bit_depth(M):
    return max(len(bin(e)[2:]) for row in M for e in row)

def test_to_bitstring():
    a = [[1, 3], [0, 2]]
    _print(a)
    assert _to_bitstring(a) == [["01", "11"], ["00", "10"]]

    b = [[2], [2]]
    _print(b)
    assert _to_bitstring(b) == [["10"], ["10"]]

if __name__ == "__main__":
    test_to_bitstring()

