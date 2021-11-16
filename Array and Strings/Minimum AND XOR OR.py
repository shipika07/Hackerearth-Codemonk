T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    min_val = 0

    A.sort()
    res = float('inf')
    for i in range(N - 1):
        res = min(res, A[i] ^ A[i + 1])

    print(res)
