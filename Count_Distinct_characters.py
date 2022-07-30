s=input()
s=s.lower()
k=sorted(set(s))
l=0
for i in k:
    if i!=" ":
        l+=1
print(l)