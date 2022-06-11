s=input()
v=input()
c=0
flag=0
for i in s:
    if i==v:
        print("True")
        print(s.index(i),end=" ")
        break
else:
    print("False")