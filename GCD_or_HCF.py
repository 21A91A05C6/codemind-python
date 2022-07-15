n,m=map(int,input().split())
o=min(n,m)
for i in range(o):
    if (n%o==0 and m%o==0):
        hcf=o
    else:
        o=o-1
print(hcf)