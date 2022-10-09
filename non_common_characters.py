s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=[]
l=[]
c=0
cc=0
m=""
for i in s2:
    if i not in s1:
        k.append(i)
for i in s1:
    if i not in s2:
        l.append(i)
k=set(k)
l=set(l)
for i in k:
    if i not in " ":
        m+=i
for i in l:
    if i not in " ":
        
        m+=i
m=sorted(m)
for i in m:
    print(i,end="")
    