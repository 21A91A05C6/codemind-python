t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    l=[]
    k=[]
    res=[]
    for i in range(n//2):
        l.append(a[i])
    for j in range(n//2,n):
        k.append(a[j])
    k=k[::-1]
    i=0
    j=0
    while(i<len(l) or i<len(k)):
        if j<len(k):
            res.append(k[j])
        j+=1
        if i<len(l):
            res.append(l[i])
        i+=1
    print(*res)