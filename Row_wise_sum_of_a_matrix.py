n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
s=0
s1=0
for i in range(n):
    s=0
    for j in range(m):
        s=s+d[i][j]
        #print(s)
    print(s,end=" ")