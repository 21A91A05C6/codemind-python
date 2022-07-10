n=int(input())
arr=list(map(int,input().split()))
k,l=map(int,input().split())
min=9
c=0
for i in arr:
    if i<k or i>l:
        if(i<min):
            c+=1
            min=i
if(c==0):
    print("-1")
else:
    print(min)