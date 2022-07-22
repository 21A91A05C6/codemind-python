n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
max=0
for i in range(n):
    s=0
    for j in range(m):
        s=s+d[i][j]
    if(s>max):
        max=s
print(max)