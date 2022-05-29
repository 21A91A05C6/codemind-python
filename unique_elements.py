n=int(input())
c=[]
a=list(map(int,input().split()))
for i in a:
    if i not in c:
        c.append(i)
print(*c)