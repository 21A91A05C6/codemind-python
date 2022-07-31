s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=""
l=""
m=""
n=""
o=""
for i in s1:
    if i not in s2 and i!=" ":
        k+=i
for i in s2:
    if i not in s1 and i!=" ":
        l+=i
m=sorted(set(k+l))
print("".join(m))