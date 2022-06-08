n=int(input())
sum=0
sum1=0
d=[list(map(int,input().split()))
for i in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j):
            sum=sum+d[i][j]
print("Principal Diagonal:",end="")
print(sum,end="")
print()
for i in range(n):
    for j in range(n):
        if(i+j==(n-1)):
            sum1=sum1+d[i][j]
print("Secondary Diagonal:",end="")
print(sum1,end="")