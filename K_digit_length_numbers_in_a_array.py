n,m=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i<0):
        i=(-i)
    #print(i,end=" ")
    if(len(str(i))==m):
        c+=1
print(c)
