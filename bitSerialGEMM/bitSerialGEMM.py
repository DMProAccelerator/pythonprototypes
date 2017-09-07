import numpy as np

def binary_gemm(A, w):
    pass 

def test():
    a = [[1, -1], 
         [-1, 1]]
    b = [[-1],
         [1]]

    print(binary_gemm(a, b))
    print(np.dot(np.asarray(a), np.asarray(b)))

if __name__ == "__main__":
    test()

