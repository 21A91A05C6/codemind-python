N, K, Q = list(map(int,input().split()))
A = list(map(int,input().split()))
    
for i in range(Q):
    x = int(input())
    print(A[(x - K) % N])
