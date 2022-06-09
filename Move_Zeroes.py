n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
for i in arr:
    if i!=0:
        a.append(i)
for i in arr:
    if i==0:
        b.append(i)
c=list(a)+list(b)
print(*c)