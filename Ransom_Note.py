s1,s2=map(str,input().split())
s2=list(s2)
for i in s1:
    if i in s2:
        s2.remove(i)
    else:
        print("False")
        break
else:
    print("True")