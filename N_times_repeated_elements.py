n=int(input())
b=[]
c=0
a=list(map(int,input().split()))
k=int(input())
for i in a:
    if k==a.count(i):
        b.append(i)
        c+=1
b=set(b)
if(c==0):
    print("-1")
else:
    print(*b)