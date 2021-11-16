T = int(input())

if(T >= 1 and T <= 20):
    for m in range(T):
        N, K = map(int,input().split())
        if(N >= 1 and N <= 100000):
            A = list(map(int,input().split()))
    
            if(K > 0 and K <= 1000000):
                if(K >= N):
                    K = K%N
                A = A[-K:] + A[:-K]              
            print(*A)
            del(A)

