n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1=set(arr1)
arr2=set(arr2)
a=[]
b=[]
c=0
c1=0
res=0
for i in arr1:
    if i not in arr2:
        c1+=1
for i in arr2:
    if i not in arr1:
        c+=1
print(c+c1)