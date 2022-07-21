n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
sum=0
for i in range(n):
    for j in range(m):
        if(i==j or (i+j)==n-1):
            sum+=d[i][j]
print(sum)