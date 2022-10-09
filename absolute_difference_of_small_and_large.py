l=list(map(str,input().split()))
for i in l:
    k=min(i)
    p=max(i)
    res=abs(ord(k)-ord(p))
    print(res,end=" ")