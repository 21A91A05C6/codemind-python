n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=[]
b=[]
for i in arr1:
    if i in arr2:
        a.append(i)
for i in a:
    if i not in b:
        b.append(i)
print(*b)