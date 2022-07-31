n=int(input())
d=list(map(int,input().split()))
sum=0
j=n-1
for i in d:
    sum=sum+i*pow(2,j)
    j-=1
print(sum)