n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if i!=1 and i!=0:
        c+=1
        #print("FALSE")
if(c==0):
    print("True")
else:
    print("False")