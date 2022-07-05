s=input()
s=s.split(" ")
b=[]
k=0
for i in s:
    c=0
    for n in i:
        if n in "aeiouAEIOU":
            c+=1
    b.append(c)
m=min(b)
for i in b:
    if i==m:
        k+=1
print(k)
