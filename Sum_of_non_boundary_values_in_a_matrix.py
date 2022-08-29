n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
sum=0
for i in range(1,n-1):
    for j in range(1,m-1):
        sum+=d[i][j]
print(sum)