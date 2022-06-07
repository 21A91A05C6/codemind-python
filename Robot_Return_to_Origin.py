s=input()
lft=0
up=0
for i in s:
    if(i=='L'):
        lft+=1
    if(i=='R'):
        lft-=1
    if(i=='U'):
        up+=1
    if(i=='D'):
        up-=1
if(lft==0 and up==0):
    print("True")
else:
    print("False")