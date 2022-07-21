n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
sum=0
for i in range(n):
    for j in range(m):
        sum=sum+d[i][j]
print(sum)