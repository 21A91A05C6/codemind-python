n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
s=0
s1=0
for i in range(m):
    s=0
    for j in range(n):
        s=s+d[j][i]
        #print(s)
    print(s,end=" ")