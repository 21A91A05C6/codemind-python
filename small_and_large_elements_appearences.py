s=input()
s=sorted(s)
k=[]
mc=0
lc=0
for i in s:
    if(i!=" "):
        k.append(i)
for i in k:
    m=i
    break
for i in k[::-1]:
    l=i
    break
for i in k:
    if(i==m):
        mc+=1
for i in k:
    if(i==l):
        lc+=1
print(m,mc,l,lc,end=" ")