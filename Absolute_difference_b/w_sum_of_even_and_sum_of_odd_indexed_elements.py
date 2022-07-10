n=int(input())
arr=list(map(int,input().split()))
sum=0
sum1=0
for i in range(len(arr)):
    if i%2==0:
        sum=sum+arr[i]
for i in range(len(arr)):
    if i%2!=0:
        sum1=sum1+arr[i]
print(abs(sum1-sum))