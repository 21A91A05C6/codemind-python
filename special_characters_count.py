s=input()
c=0
for i in s:
    if i in "!~@#$%^&*()_+|}{:?><`1234567890-=[]\;',./":
        c+=1
print(c)