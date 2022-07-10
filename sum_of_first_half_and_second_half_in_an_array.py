n=int(input())
arr=list(map(int,input().split()))
sum=0
sum1=0
for i in range(0,n//2):
    sum=sum+arr[i]
for i in range(n//2,n):
    sum1=sum1+arr[i]
print(sum)
print(sum1)