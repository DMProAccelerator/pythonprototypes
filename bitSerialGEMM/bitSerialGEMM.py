import numpy as np
import random
from utils import _print, to_bitstring, flatten, transpose, \
    popcount, _and

def binary_gemm(W, A, alpha=None):
    rows = len(W)
    cols = len(A)
    R = [0] * rows
    for r in range(rows):
        for c in range(cols):
            t1 = W[r][c]
            t2 = A[c]
            R[r] += popcount(_and(t1, t2))
    return R

def test_binary_gemm():
    W = [[0, 0, 0, 1, 1, 1, 0, 0],
         [1, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 1]]
    A = [0, 1, 1, 1, 1, 1, 1, 0]
    assert binary_gemm(to_bitstring(W), to_bitstring(A)) \
            == np.dot(np.asarray(W), np.asarray(A)).tolist()

    W = [[1, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1]]
    A = [0, 0, 0, 1, 1, 0, 1, 0]
    assert binary_gemm(to_bitstring(W), to_bitstring(A)) \
            == np.dot(np.asarray(W), np.asarray(A)).tolist()

def test_random_binary_gemm():
    for _ in range(100):
        # random vector
        A = np.random.randint(0, 2, random.randint(1, 50))
        # random matrix
        W = np.random.randint(0, 2, 
                size=(random.randint(1, 50), A.shape[0]))

        assert np.dot(W, A).tolist() \
                == binary_gemm(to_bitstring(W.tolist()), \
                                to_bitstring(A.tolist()))


if __name__ == "__main__":
    test_binary_gemm()
    test_random_binary_gemm()

