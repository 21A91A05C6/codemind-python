s=input()
s=s.split(" ")
b=[]
max=0
for i in s:
    c=0
    for n in i:
        if n in "aeiouAEIOU":
            c+=1
    if max<c:
        max=c
print(max)
