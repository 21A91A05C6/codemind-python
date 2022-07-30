s=input()
k=[]
l=[]
h=[]
c=0
for i in s:
    k.append(s.count(i))
m=max(k)
for i in s:
    if s.count(i)!=m:
        l.append(i)
        c+=1
for i in l:
    h.append(l.count(i))
#l.remove(m)
for i in h:
    h1=max(h)
    break
if(c==0):
    print("-1")
else:
    for i in l:
        if s.count(i)==h1:
            print(i)
            break