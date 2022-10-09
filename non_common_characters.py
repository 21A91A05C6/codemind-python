s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=""
m=""
for i in s2:
    if i not in s1:
        k+=i
for i in s1:
    if i not in s2:
        k+=i
for i in k:
    if i not in " ":
        m+=i
m=sorted(set(m))
for i in m:
    print(i,end="")
    