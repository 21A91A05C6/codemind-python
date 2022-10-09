s=input().split()
c=0
s=set(s[-1])
m=min(s)
for i in s:
    if ord(m)+32==ord(i):
        print(i)
        c+=1
        break
if(c==0):
    print(m)