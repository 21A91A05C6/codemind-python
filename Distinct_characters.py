s=input()
s=s.lower()
l=""
for i in s:
    if s.count(i)==1 and i!=" ":
        l+=i
print("".join(sorted(l)))