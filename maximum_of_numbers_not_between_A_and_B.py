n=int(input())
arr=list(map(int,input().split()))
k,l=map(int,input().split())
max=0
c=0
for i in arr:
    if i<k or i>l:
        if(i>max):
            c+=1
            max=i
if(c==0):
    print("-1")
else:
    print(max)