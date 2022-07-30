n=int(input())
d=list(map(int,input().split()))
k,l=map(int,input().split())
min=9
c=0
#print(k,l,end=" ")
#print()
for i in d:
    if i<k or i>l:
        #print(i,end=" ")
        if(min>i):
            min=i
            c+=1
if(c==0):
    print("-1")
else:
    print(min)
#print(d,end=" ")