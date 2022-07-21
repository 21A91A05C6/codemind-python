n,m=map(int,input().split())
d=[list(map(int,input().split()))
for i in range(n)]
sum=0
sum1=0
for i in range(n):
    for j in range(m):
        if(d[i][j]%2==0):
            sum=sum+d[i][j]
        else:
            sum1=sum1+d[i][j]
print(sum,sum1,end=" ")