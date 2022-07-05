s=input()
v=input()
c=0

for i in s:
    if i==v:
        c+=1
        print("True")
        print(s.index(i))
        break
if(c==0):
    print("False")