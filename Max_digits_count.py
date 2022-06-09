n=int(input())
arr=list(map(str,input().split()))
b=[]
c=0
for i in arr:
   # print(i)
    b.append(len(i))
m=max(b)
for i in arr:
    if(len(i)==m):
        c+=1
print(c)