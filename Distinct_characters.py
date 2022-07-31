s=input()
s=s.lower()
l=""
s=set(s)
for i in s:
    if i!=" ":
        l+=i
print("".join(sorted(l)))