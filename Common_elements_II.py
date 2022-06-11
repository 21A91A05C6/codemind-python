n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=[]
b=[]
for i in arr1:
    if i not in arr2:
        a.append(i)

for i in arr2:
    if i not in arr1:
        b.append(i)
c=list(a)+list(b)
print(*c)