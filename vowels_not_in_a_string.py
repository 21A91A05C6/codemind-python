s=input()
c=0
k=""
v="aeiou"
s1=""
for i in s:
    if i not in k:
        k+=i
for i in k:
    if i in v:
        s1+=i
for i in v:
    if i not in s1:
        c+=1
        print(i,end=" ")
if(c==0):
    print("0")