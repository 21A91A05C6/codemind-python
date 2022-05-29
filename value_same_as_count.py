n=int(input())
b=[]
a=list(map(int,input().split()))
for i in a:
    if i==a.count(i):
        b.append(i)
b=set(b)
print(len(b))