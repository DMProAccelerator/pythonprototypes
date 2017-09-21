import numpy as np
from binary_gemm import binary_gemm
from utils import to_bitstring, _and, add_lists

def bitserial_gemm(W, A):
    R = [0]*len(W)
    for i in range(len(W[0][0])):
        for j in range(len(A[0])):
            # build A vector
            tA = [e[j] for e in A]
            # build W matrix
            rows = len(W)
            cols = len(W[0])
            tW = [[] for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    tW[r].append(W[r][c][i])
            alpha = 2**(i+j)
            R = add_lists(R, binary_gemm(tW, tA, alpha))
    return R

def test():
    A = [8,0,2]
    W = [[2,3,5],[1,0,4]]
    print(bitserial_gemm(to_bitstring(W), to_bitstring(A)))
    print(np.dot(np.asarray(W), np.asarray(A)))


if __name__ == "__main__":
    test()

