s=input()
s=s.lower()
k=sorted(set(s))
l=""
for i in k:
    if i!=" ":
        l+=i
print(l)