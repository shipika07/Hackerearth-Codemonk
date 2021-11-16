import numpy as np

def ans(n):
    matrix = np.array([[99,-10],[10,-1]])
    is_even = 1
    if(n%2 != 0):
        n = n+1
        is_even =0
        
    n_power = n/2 - 1
    power = np.linalg.matrix_power(matrix, int(n_power))
    
    if(is_even):
            return power[0][0] * 99 + power[0][1] * 10
    else:
            return power[1][0] * 99 + power[1][1] * 10


T = int(input())

for _ in range(T):
    N = int(input())
    print(ans(N))

