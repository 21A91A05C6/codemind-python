n=int(input())
arr=list(map(int,input().split()))
b=[]
c=0
for i in arr:
    if(arr.count(i)==1):
        c+=1
        b.append(i)
if(c==0):
    print("-1")
else:
    
    print(*b)