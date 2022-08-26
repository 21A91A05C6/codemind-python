s=input()
c=1
res=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
        res=max(res,c)
    else:
        c=1
print(res)