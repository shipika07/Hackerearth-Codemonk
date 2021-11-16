T = int(input())

for m in range(T):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if(A[i][j] > A[k][l] and i <= k and j <= l):
                            count = count + 1
    print(count)