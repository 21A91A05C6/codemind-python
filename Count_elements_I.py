n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
c=0
b=set(b)
d=a.intersection(b)
for i in d:
    c+=1
print(c)