s=input()
s=s.lower()
l=0
for i in s:
    if s.count(i)==1 and i!=" ":
        l+=1
print(l)