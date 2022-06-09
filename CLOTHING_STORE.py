n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
sum=0
c=0
for i in arr:
    if(arr.count(i)>1):
        a.append(i)
a=set(a)
for i in a:
    c=arr.count(i)//2
    sum=sum+c
print(sum)