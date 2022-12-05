n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
l=[]
for i in b:
    if i in a:
        c+=1
        l.append(i)
        a.remove(i)
if l==b:
    print("Yes")
else:
    print("No")
'''print(a)
print(b)
print(c)
print(l)'''