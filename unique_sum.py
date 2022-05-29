n=int(input())
a=list(map(int,input().split()))
a=set(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
    