s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=[]
l=[]
c=0
for i in s2:
    if i in s1:
        k.append(i)
for i in k:
    if i not in l and i!=" ":
        l.append(i)
for i in l:
    c+=1
print(c)