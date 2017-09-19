import numpy as np
import pprint
from utils import _print, _to_bitstring

def _xor(a, b):
    return a != b

def _and(a, b):
    return "".join("1" for x,y in zip(a, b)
            if x == "1" and y == "1")

def popcount(b):
    return b.count("1")

def gemm(A, W, alpha=None):
    R = [[0]]*len(W)
    print(R)
    for i in range(len(W)):
        for j in range(len(A[0])):
            x = W[i][0]
            y = A[i][j]
            print(x, y)
            tmp = _and(x, y)
            print("tmp:", tmp)
            R[i][0] += popcount(tmp)
    return R
    

def test():
    a = [[0, 1], [0, 1]]
    b = [[0], [1]]
    _print(a, "A")
    _print(_to_bitstring(a))
    _print(b, "W")
    _print(_to_bitstring(b))


    print(gemm(_to_bitstring(a), _to_bitstring(b)))
    print(np.dot(np.asarray(a), np.asarray(b)))

if __name__ == "__main__":
    test()

