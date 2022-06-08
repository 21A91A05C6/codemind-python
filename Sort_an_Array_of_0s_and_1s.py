n=int(input())
arr=list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in arr:
    if(i==0):
        b.append(i)
for i in arr:
    if(i==1):
        c.append(i)
d=b+c
print(*d)