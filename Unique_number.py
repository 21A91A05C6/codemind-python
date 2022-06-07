n=int(input())
a=[]
b=[]
c=0
dc=0
while(n>0):
    d=n%10
    n=n//10
    dc+=1
    a.append(d)
for i in a:
    if i not in b:
        b.append(i)
        c+=1
if(c==dc):
    print("Unique Number")
else:
    print("Not Unique Number")
        