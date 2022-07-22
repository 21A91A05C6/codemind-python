n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
s=0
s1=0
for i in range(n):
    for j in range(m):
        if i%2==0:
            s=s+d[i][j]
for i in range(n):
    for j in range(m):
        if i%2!=0:
            s1=s1+d[i][j]
print(s,s1,end=" ")
