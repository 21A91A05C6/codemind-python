s=input()
c=0
k=""
v="aeiou"
for i in s:
    if i not in k:
        k+=i
for i in k:
    if i in v:
        c+=1
if(c==5):
    print("True")
else:
    print("False")