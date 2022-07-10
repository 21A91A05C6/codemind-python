n=int(input())
arr=list(map(int,input().split()))
sum=0
sum1=0
for i in arr:
    if i%2==0:
        sum=sum+i
for i in arr:
    if i%2!=0:
        sum1=sum1+i
print(abs(sum1-sum))