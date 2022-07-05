s=input()
l=len(s)
c=0
for i in s:
    if s.count(i)==1:
        c+=1
if(c==l):
    print("True")
else:
    print("False")