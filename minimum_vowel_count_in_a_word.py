s=input()
s=s.split(" ")
b=[]
min=9
for i in s:
    c=0
    for n in i:
        if n in "aeiouAEIOU":
            c+=1
    if min>c:
        min=c
print(min)
