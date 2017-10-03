import numpy as np
from utils import to_bitstring, add_lists

def bitserial_gemm(W, A):
    """
    Assume that W is a matrix and A is a vector
    Both contain only bitstring representations of signed integers
    """
    R = [0]*len(W)
    w = len(W[0][0])
    a = len(A[0])
    for i in range(w):
        for j in range(a):
            # build A bitplanes
            bA = [e[j] for e in A]
            # build W bitplanes
            bW = [[e[i] for e in row] for row in W]
            # make sure significance is big endian
            # because we represent bitstrings with MSB first
            alpha = 2**((len(W[0][0])-i-1)
                        +(len(A[0])-j-1))
            # bitstrings have MSB as first index, needs to be reflected in signs
            signW = -1 if i == 0 else 1
            signA = -1 if j == 0 else 1
            R = add_lists(R, binary_gemm(bW, bA, signW * signA * alpha))
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

def bitserial_gemm_wrapper(a, b):
    """
    Emulate numpy.dot using bitserial_gemm
    a and b are numpy arrays
    """
    res = bitserial_gemm(to_bitstring(a.tolist()), to_bitstring(b.tolist()))
    return np.asarray(res)


def test():
    A = [5, 10, -100]
    W = [[1,0,0],[0,1,0], [0,0,1]]
    print(bitserial_gemm_wrapper(np.asarray(W), np.asarray(A)))
    print(np.dot(np.asarray(W), np.asarray(A)))


if __name__ == "__main__":
    test()

