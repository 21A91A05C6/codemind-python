s1=input()
s2=input()
s1=s1.split(" ")
s2=s2.split(" ")
k=[]
l=[]
c=0
for i in s1:
    if s1.count(i)==1:
        k.append(i)
for i in s2:
    if s2.count(i)==1:
        l.append(i)
for i in k:
    if i in l:
        c+=1
print(c)