s=input()
t=input()
k=""
l=""
for i in s:
    if i=='#':
        k=k[:-1]
    else:
        k+=i
for i in t:
    if i=='#':
        l=l[:-1]
    else:
        l+=i
if(k==l):
    print("True")
else:
    print("False")
    