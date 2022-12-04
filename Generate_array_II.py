n=int(input())
a=list(map(int,input().split()))
l=[]
k=[]
res=[]
for i in range(0,n):
    if i%2==0:
        l.append(a[i])
    else:
        k.append(a[i])
#print(l)
#print(k)
i=0
j=0
while(i<len(l) or j<len(k)):
    if i<len(l) and j<len(k):
        for s in range(k[j]):
            res.append(l[i])
    i+=1
    j+=1
print(*res)