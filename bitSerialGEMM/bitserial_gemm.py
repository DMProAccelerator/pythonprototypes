import numpy as np
from utils import to_bitstring, add_lists

def bitserial_gemm(W, A):
    R = [0]*len(W)
    w = len(W[0][0])
    a = len(A[0])
    for i in range(w):
        for j in range(a):
            # build A bitplanes
            tA = [e[j] for e in A]
            # build W bitplanes
            rows = len(W)
            cols = len(W[0])
            tW = [[] for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    tW[r].append(W[r][c][i])
            # make sure significance is big endian
            # because we represent bitstrings with MSB first
            alpha = 2**((len(W[0][0])-i-1)
                        +(len(A[0])-j-1))
            R = add_lists(R, binary_gemm(tW, tA, alpha))
    return R


def binary_gemm(W, A, alpha=None):
    """Operate on lists of booleans, return a list of ints"""
    rows = len(W)
    cols = len(A)
    R = [0] * rows
    for r in range(rows):
        for c in range(cols):
            t1 = W[r][c]
            t2 = A[c]
            # Since we are working with individual bits we dont popcount
            if alpha:
                R[r] += alpha * int(t1 & t2)
            else:
                R[r] += int(t1 & t2)
    return R


def test():
    A = [8,0,2]
    W = [[2,3,5],[1,0,4]]
    print(bitserial_gemm(to_bitstring(W), to_bitstring(A)))
    print(np.dot(np.asarray(W), np.asarray(A)))


if __name__ == "__main__":
    test()

