s=input()
c=0
k=""
v="aeiouAEIOU"
s1=""
for i in s:
    if i not in k:
        k+=i
for i in k:
    if i in v:
        c+=1
        print(i,end=" ")
if(c==0):
    print("-1")