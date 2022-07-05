s=input()
s=s.split(" ")
c=0
for i in s:
    c=0
    for n in i:
        #c=0
        if n in "aeiouAEIOU":
            c+=1
    print(c,end=" ")