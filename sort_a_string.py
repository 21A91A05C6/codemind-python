s=input()
sort=""
res=""
for i in s:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        sort+=i
sort=sorted(sort)
j=0
for i in s:
    if i not in "~`!@#$%^&*()_+=-|\{}][:;'' /?":
        res+=sort[j]
        j+=1
    else:
        res+=i
print(res)