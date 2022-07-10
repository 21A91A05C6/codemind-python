n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
h=[]
for i in arr:
    if arr.count(i)==k:
        c+=1
        h.append(i)
h=set(h)
if(c==0):
    print("-1")
else:
    print(*set(h))